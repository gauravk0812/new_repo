import os
from pathlib import Path
from typing import BinaryIO
from uuid import UUID
from fastapi import UploadFile
from fastapi_injector import Injected
from injector import inject
from pylekhagaar.app_settings import AppSettings
from pylekhagaar.core.contracts.idocument_permission_checker import IDocumentPermissionChecker
from pylekhagaar.core.contracts.idocument_repository import IDocumentRepository
from pylekhagaar.core.contracts.idocument_service import IDocumentService
from pylekhagaar.core.contracts.idocument_storage_type_repository import IDocStorageTypeRepository
from pylekhagaar.core.contracts.istorage_provider import IStorageProvider
from pylekhagaar.core.contracts.istorage_provider_factory import IStorageProviderFactory
from pylekhagaar.core.enum.storage_type_enum import StorageTypeEnum
from pylekhagaar.helpers.helper_functions import DocumentLocationGenerator, guess_mime
from pylekhagaar.core.schemas.document import Document
from pycrud.core.exceptions.not_found_exception import NotFoundException
from pycrud.service.base_tenant_service_impl import BaseTenantServiceImpl


config = AppSettings()
TEMP_DIRECTORY = Path(config.TEMP_DIRECTORY)
TEMP_DIRECTORY.mkdir(exist_ok=True)


class DocumentServiceImpl(IDocumentService, BaseTenantServiceImpl[Document]):
    """Implementation of Document service operations."""

    def must_implement(self) -> None:
        pass

    
    @inject
    def __init__(self,
                document_repository: IDocumentRepository = Injected(IDocumentRepository),
                permission_checker: IDocumentPermissionChecker = Injected(IDocumentPermissionChecker),
                docstorage_type: IDocStorageTypeRepository = Injected(IDocStorageTypeRepository),
                storage_provider_factory:IStorageProviderFactory = Injected(IStorageProviderFactory),
                # doc_location_generator: DocumentLocationGenerator = Injected(DocumentLocationGenerator)
                ):

        super().__init__(Document, document_repository, permission_checker)

        # # Initialize the repository and permission checker
        self._document_repository: IDocumentRepository = document_repository
        self._permission_checker: IDocumentPermissionChecker = permission_checker
        self._docstorage_type: IDocStorageTypeRepository = docstorage_type
        self._storage_provider_factory = storage_provider_factory
        # self.doc_location_generator = doc_location_generator


    def get_by_id(self, id: UUID) -> Document:
        """ Get a document by its ID.
        :param document_id: UUID of the document to retrieve.
        :return: Document object with metadata (physical_path is cleared).
        """
        document = self._document_repository.get_by_id(id)
        if document:
            # Hide physical_path before exposing metadata
            document.physical_path = None

        if not document:
            raise NotFoundException(detail="Document not found for specified Id")
        
        return document


    def add(self, item: Document) -> Document:
        """ Add a new document.
        :param document: Document object to be added.
        :return: Added Document object with metadata (physical_path is cleared).
        """

        # extracting MIME type from document name
        if item.name is not None:
            item.mime_type = guess_mime(item.name)

        savedDocumentMeta = super().add(item)
        return savedDocumentMeta
    

    def set_document_content(self, document_id: UUID, source_file_location: UploadFile) -> Document:
        """ Set or update the content of a document by uploading a file.
        :param document_id: UUID of the document to update.
        :param source_file: UploadFile object containing the file to upload.
        :return: Updated Document object with metadata (physical_path is cleared).
        """
        document = super().get_by_id(document_id)
        if not document:
            raise NotFoundException(detail="Document not found for specified Id")

        storage_type: IStorageProvider = self._storage_provider_factory.get_storage_provider(document.storage_id)
        document:Document = storage_type.set_document_content(document_id, source_file_location)
        
        return document


    def get_document_content(self, document_id: UUID) -> tuple[BinaryIO, str]:
        """ Get the file content of a document by its ID.
        :param document_id: UUID of the document to retrieve.
        :return: Tuple containing a binary stream of the file content and the filename.
        """
        document = super().get_by_id(document_id)
        if not document:
            raise NotFoundException(detail="Document not found for specified Id")
        
        storage_type: IStorageProvider = self._storage_provider_factory.get_storage_provider(document.storage_id)
        return storage_type.get_document_content(document_id)
    

    def delete_document(self, document_id: UUID) -> bool:
        """ Delete a document by its ID.
        :param document_id: UUID of the document to delete.
        :return: True if deletion was successful, False otherwise.
        """
        document = super().get_by_id(document_id)
        if not document:
            raise NotFoundException(detail="Document not found for specified Id")
        
        storage_type: IStorageProvider = self._storage_provider_factory.get_storage_provider(document.storage_id)
        return storage_type.delete_document_content(document_id)


    
    
    