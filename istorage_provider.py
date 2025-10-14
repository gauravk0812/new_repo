from abc import ABC
from abc import abstractmethod
from typing import BinaryIO
from uuid import UUID
from fastapi import UploadFile
from pylekhagaar.core.enum.storage_type_enum import StorageTypeEnum
from pylekhagaar.core.schemas.document import Document
from pylekhagaar.core.schemas.storage_type import DocStorageType


class IStorageProvider(ABC):



    @property
    @abstractmethod
    def storage_type(self) -> StorageTypeEnum:
        """ Returns the type of storage provider. """
        raise NotImplementedError()
    
    
    @abstractmethod
    def initialize(self, storage_type: DocStorageType) -> None:
        """ Initialize the storage provider with necessary authentication details.
        :param authenticator_details: Details required to authenticate with the storage service.
        """
        raise NotImplementedError()
    


    @abstractmethod
    def set_document_content(self, document_id: UUID, source_file_location: UploadFile) -> Document:
        """
        Set or update the content of a document.
        :param document_id: The unique identifier of the document.
        :param source_file_location: The file path where the new content is located.
        :return: The updated Document with new content information.
        """
        raise NotImplementedError()
    
    @abstractmethod
    def get_document_content(self, document_id: UUID) -> tuple[BinaryIO, str]:
        """
        Retrieve the content of a document as a binary stream.
        :param document_id: The unique identifier of the document.
        :return: A binary stream of the document's content.
        """
        raise NotImplementedError()
    
    @abstractmethod
    def delete_document_content(self, document_id: UUID) -> bool:
        """
        Deletes both the metadata entry and the physical file (if it exists).
        Returns True if deleted, False otherwise.
        :param document_id: The unique identifier of the document to be deleted.
        :return: A boolean indicating whether the document was successfully deleted.
        """
        raise NotImplementedError()