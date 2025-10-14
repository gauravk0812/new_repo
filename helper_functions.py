from datetime import datetime, timezone
import mimetypes
import os
from pathlib import Path

from pylekhagaar.app_settings import AppSettings
from pylekhagaar.core.schemas.document import Document

def guess_mime(file_path: str) -> str:
    """
    Guess MIME type from a file path or extension.
    Falls back to 'application/octet-stream' if unknown.
    """
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type or "application/octet-stream"


class DocumentLocationGenerator:

    config = AppSettings()
    BASE_DOC_STORE_DIRECTORY = Path(config.BASE_DOC_STORE_DIRECTORY)
    BASE_DOC_STORE_DIRECTORY.mkdir(exist_ok=True)

    def __init__(self,file_limit: int = 100):
        self.file_limit = file_limit


    def generate_doc_location(self, document: Document | None) -> str:
        """
        Generate a physical storage path for the document.
        Replicates the C# GenerateDocLocation behavior.
        """

        if document is None:
            raise ValueError("document cannot be None")

        # Ensure created_at is set (similar to C# DateTimeProvider.Now)
        if not getattr(document, "created_at", None):
            document.created_at = datetime.now(timezone.utc)

        # Build directory path: BaseDir/Tenant/Category/Year/Month/Day/Hour
        path = os.path.join(
            self.BASE_DOC_STORE_DIRECTORY,
            str(document.created_at.year),
            str(document.created_at.month),
            str(document.created_at.day),
            str(document.created_at.hour),
        )

        os.makedirs(path, exist_ok=True)

        # Optionally create a "sequence folder" (C# had CreateSequenceFolder)
        sequence_folder_path = self._create_sequence_folder(path)

        return sequence_folder_path
    

    def _create_sequence_folder(self, base_category_path: str) -> str:
        """
        Creates or selects a sequence-based subfolder under base_category_path.
        - Starts with 0001 if none exists.
        - If last folder reaches file_limit, create next (0002, 0003, etc.)
        - Returns the folder path.
        """
        # Get all existing subfolders
        directories = [
            d for d in os.listdir(base_category_path)
            if os.path.isdir(os.path.join(base_category_path, d))
        ]
        directories.sort()

        if not directories:
            # No subfolder exists, create 0001
            sequence_folder_path = os.path.join(base_category_path, "0001")
            os.makedirs(sequence_folder_path, exist_ok=True)
            return sequence_folder_path

        # Use last directory
        last_directory = directories[-1]
        last_directory_path = os.path.join(base_category_path, last_directory)

        # Count files in last directory
        file_count = len([
            f for f in os.listdir(last_directory_path)
            if os.path.isfile(os.path.join(last_directory_path, f))
        ])

        if file_count >= self.file_limit:
            # Create new sequence folder
            sequence_no = int(last_directory) + 1
            new_sequence_folder = f"{sequence_no:04d}"  # zero-padded like 0002
            new_sequence_folder_path = os.path.join(base_category_path, new_sequence_folder)
            os.makedirs(new_sequence_folder_path, exist_ok=True)
            return new_sequence_folder_path

        # Use existing folder
        return last_directory_path