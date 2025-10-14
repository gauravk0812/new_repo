from pathlib import Path
from typing import BinaryIO
from pylekhagaar.core.contracts.istorage_provider import IStorageProvider
from fastapi_injector import Injected
from pylekhagaar.core.contracts.istorage_provider import IStorageProvider
from pylekhagaar.core.contracts.idocument_repository import IDocumentRepository
from injector import inject

from pylekhagaar.core.enum.storage_type_enum import StorageTypeEnum
from pylekhagaar.core.schemas.storage_type import DocStorageType
from pycrud.core.exceptions.not_found_exception import NotFoundException

from pylekhagaar.helpers.helper_functions import DocumentLocationGenerator
import os

from uuid import UUID
from fastapi import UploadFile
from fastapi_injector import Injected
from injector import inject
from pylekhagaar.app_settings import AppSettings
from pylekhagaar.core.contracts.idocument_repository import IDocumentRepository
from pylekhagaar.core.contracts.istorage_provider import IStorageProvider
from pylekhagaar.core.enum.storage_type_enum import StorageTypeEnum
from pylekhagaar.helpers.helper_functions import DocumentLocationGenerator, guess_mime
from pylekhagaar.core.schemas.document import Document
from pycrud.core.exceptions.not_found_exception import NotFoundException
from pycrud.core.contracts.icrud_logger import ICrudLogger

config = AppSettings()
TEMP_DIRECTORY = Path(config.TEMP_DIRECTORY)
TEMP_DIRECTORY.mkdir(exist_ok=True)

class LocalFileStorageProviderImpl(IStorageProvider):
    @inject
    def __init__(self,
                document_repository: IDocumentRepository = Injected(IDocumentRepository),
                logger: ICrudLogger = Injected(ICrudLogger),
                ):
            self._document_repository: IDocumentRepository = document_repository
            self._logger = logger.get_logger(__name__)


    @property
    def storage_type(self) -> StorageTypeEnum:
        return StorageTypeEnum.LOCAL_FS

    def initialize(self, storage_type: DocStorageType) -> None:
        assert storage_type.storageType == StorageTypeEnum.LOCAL_FS, "Authenticator type must be AZURE_BLOB"
        self._logger.info("Initialized Azure Blob Storage Provider")



    def set_document_content(self, document_id: UUID, source_file_location: UploadFile) -> Document:
        """ Set or update the content of a document by uploading a file.
        :param document_id: UUID of the document to update.
        :param source_file: UploadFile object containing the file to upload.
        :return: Updated Document object with metadata (physical_path is cleared).
        """
        document =self._document_repository.get_by_id(document_id)
        if not document:
            raise NotFoundException(detail="Document not found for specified Id")


        # Generate destination file path
        doclocationGenerator = DocumentLocationGenerator()
        destination_folder_path = doclocationGenerator.generate_doc_location(document)

        new_file_name = f"{document.id}_{source_file_location.filename}"
        destination_file_path = os.path.join(destination_folder_path, new_file_name)

        # If old file exists, delete it
        if document.physical_path and os.path.exists(document.physical_path):
            os.remove(document.physical_path)

        # Ensure temp directory exists
        os.makedirs(TEMP_DIRECTORY, exist_ok=True)

        # Write uploaded file to destination
        with open(destination_file_path, "wb") as dest_file:
            while chunk := source_file_location.file.read(1024 * 1024):  # write in chunks (1 MB)
                dest_file.write(chunk)

        # Update database with new physical path
        document.name = source_file_location.filename
        document.physical_path = destination_file_path
        document.mime_type = guess_mime(destination_file_path)
        
        updated = self._document_repository.update(document)

        # Clear path before returning (to mimic C#)
        updated.physical_path = None
        return updated
    
    def get_document_content(self, document_id: UUID) -> tuple[BinaryIO, str]:
        """ Get the file content of a document by its ID.
        :param document_id: UUID of the document to retrieve.
        :return: Tuple containing a binary stream of the file content and the filename.
        """
        return self._document_repository.get_document_content(document_id)
    


    
    def delete_document_content(self, document_id: UUID) -> bool:
        """ Deletes both the metadata entry and the physical file (if it exists).
            Returns True if deleted, False otherwise."""

        document = self._document_repository.get_by_id(document_id)
        if not document:
            raise NotFoundException("Document not found")

        # Delete metadata entry
        return self._document_repository.delete_document(document_id)