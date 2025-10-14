import os
from typing import BinaryIO
from uuid import UUID
from fastapi_injector import Injected
from injector import inject
from sqlalchemy.orm import Session
from pylekhagaar.core.contracts.idocument_repository import IDocumentRepository
from pylekhagaar.core.schemas.document import Document
from pylekhagaar.modules.document.document_model import DocumentModel
from pycrud.core.contracts.icrud_logger import ICrudLogger
from pycrud.core.contracts.icurrent_user_provider import ICurrentUserProvider
from pycrud.core.contracts.idatetime_provider import IDateTimeProvider
from pycrud.core.exceptions.not_found_exception import NotFoundException
from pycrud.repository.base_tenant_repository_impl import BaseTenantRepositoryImpl
from pycrud.core.schemas.paged_result import PagedResult
from pycrud.core.contracts.idata_filter import IDataFilter
from pycrud.core.contracts.itenant_provider import ITenantProvider


class DocumentRepositoryImpl(IDocumentRepository, BaseTenantRepositoryImpl[Document, DocumentModel]):
    """Implementation of Document repository operations."""

    def must_implement(self) -> None:
        pass
    
    @inject
    def __init__(self,
                 logger: ICrudLogger = Injected(ICrudLogger),
                 session: Session = Injected(Session),
                 tenant_provider: ITenantProvider = Injected(ITenantProvider),
                 current_user_provider: ICurrentUserProvider = Injected(ICurrentUserProvider),
                 date_time_provider: IDateTimeProvider = Injected(IDateTimeProvider),
                 ) -> None:
        
        super().__init__(
                        logger=logger.get_logger(__name__),
                        db_session=session,
                        tenant_provider=tenant_provider,
                        current_user_provider=current_user_provider,
                        date_time_provider=date_time_provider,
                        item_schema=Document,
                        item_db_model=DocumentModel)



    def find(self,data_filter: IDataFilter,page_index: int = -1,page_size: int = 10
    ) -> PagedResult[Document]:
        # Call the base method
        result = super().find(data_filter, page_index, page_size)

        # Ensure physical_path is None for all items
        for item in result.items:
            item.physical_path = None

        return result

        
    def get_document_content(self, document_id: UUID) -> tuple[BinaryIO, str|None]:
        """
        Returns (file_stream, filename) without exposing physical_path.
        """
        document = super().get_by_id(document_id)
        if not document:
            raise NotFoundException(detail=f"Document not found for ID: {document_id}")

        if not document.physical_path or not os.path.exists(document.physical_path):
            raise NotFoundException(detail=f"Document file not found for ID: {document_id}")

        file_stream = open(document.physical_path, "rb")
            
        return file_stream, document.name
    

    def delete_document(self, document_id: UUID) -> bool:
        """
        Deletes both the metadata entry and the physical file (if it exists).
        Returns True if deleted, False otherwise.
        """
        document = super().get_by_id(document_id)
        if not document:
            raise NotFoundException(detail=f"Document not found for ID: {document_id}")

        # Delete file if exists
        if document.physical_path and os.path.exists(document.physical_path):
            os.remove(document.physical_path)

        # Delete metadata from database
        super().delete(document_id)

        return True