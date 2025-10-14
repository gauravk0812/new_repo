from io import BytesIO
from typing import BinaryIO
from uuid import UUID
from fastapi import UploadFile
from fastapi_injector import Injected
from injector import inject
from pylekhagaar.core.contracts.idocument_repository import IDocumentRepository
from pylekhagaar.core.contracts.idocument_storage_type_repository import IDocStorageTypeRepository
from pylekhagaar.core.enum.storage_type_enum import StorageTypeEnum
from pylekhagaar.core.schemas.storage_type import DocStorageType
from pylekhagaar.helpers.helper_functions import guess_mime
from pylekhagaar.core.schemas.document import Document
from pycrud.core.exceptions.not_found_exception import NotFoundException
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceExistsError

from fastapi_injector import Injected
from pylekhagaar.core.contracts.istorage_provider import IStorageProvider
from pylekhagaar.core.contracts.idocument_repository import IDocumentRepository
from injector import inject
from pycrud.core.contracts.icrud_logger import ICrudLogger



class AzureBlobStorageProviderImpl(IStorageProvider):
    @inject
    def __init__(self,
                document_repository: IDocumentRepository = Injected(IDocumentRepository),
                storage_type_repository: IDocStorageTypeRepository = Injected(IDocStorageTypeRepository),
                logger: ICrudLogger = Injected(ICrudLogger),
                ):
            self._document_repository: IDocumentRepository = document_repository
            self._storage_type_repository: IDocStorageTypeRepository = storage_type_repository
            self._logger = logger.get_logger(__name__)

            


    @property
    def storage_type(self) -> StorageTypeEnum:
        return StorageTypeEnum.AZURE_BLOB

    def initialize(self, storage_type: DocStorageType) -> None:
        assert storage_type.storageType == StorageTypeEnum.AZURE_BLOB

        config = storage_type.configParam
        conn_str = self._build_connection_string(config)
        container_name = config.get("container_name", "documents")

        self.blob_service_client = BlobServiceClient.from_connection_string(conn_str)
        self.container_client = self.blob_service_client.get_container_client(container_name)

        # Ensure container exists
        try:
            self.container_client.create_container()
        except ResourceExistsError:
            pass

        self._logger.info("Initialized Azure Blob Storage Provider")

        

    def set_document_content(self, document_id: UUID, source_file_location: UploadFile) -> Document:
        """ Set or update the content of a document by uploading a file.
        :param document_id: UUID of the document to update.
        :param source_file: UploadFile object containing the file to upload.
        :return: Updated Document object with metadata (physical_path is cleared).
        """
        document = self._document_repository.get_by_id(document_id)
        if not document:
            raise NotFoundException(detail="Document not found for specified Id")
            
        """
        Upload file stream to Azure Blob and return blob name.
        """
        # self._initialize_blob_client(document.storage_id)


        blob_name = f"{document.id}/{source_file_location.filename}"
        blob_client = self.container_client.get_blob_client(blob_name)

        # Reset file pointer and upload
        source_file_location.file.seek(0)
        blob_client.upload_blob(source_file_location.file, overwrite=True)

        document.physical_path = blob_name
        document.name = source_file_location.filename
        document.mime_type = guess_mime(source_file_location.filename)

        updated_doc_details = self._document_repository.update(document)
        updated_doc_details.physical_path = None

        return updated_doc_details
    

    def get_document_content(self, document_id: UUID) -> tuple[BinaryIO, str]:
        """ Get the file content of a document by its ID.
        :param document_id: UUID of the document to retrieve.
        :return: Tuple containing a binary stream of the file content and the filename.
        """

        document = self._document_repository.get_by_id(document_id)
        if not document:
            raise NotFoundException("Document not found")

        # self._initialize_blob_client(document.storage_id)
        """
        Download blob and return BytesIO stream.
        """
        blob_client = self.container_client.get_blob_client(document.physical_path)
        downloader = blob_client.download_blob()
        stream = BytesIO(downloader.readall())
        stream.seek(0)  
        return stream, document.name
    

    def delete_document_content(self, document_id: UUID) -> bool:
        """ Delete the blob content of a document by its ID.
        :param document_id: UUID of the document to delete.
        :return: True if deletion was attempted (even if blob not found).
        """
        document = self._document_repository.get_by_id(document_id)
        if not document:
            raise NotFoundException("Document not found")

        # Ensure blob client is initialized
        # self._initialize_blob_client(document.storage_id)

        if not document.physical_path:
            self._logger.warning(f"No blob path set for document {document.id}")
            return False

        blob_client = self.container_client.get_blob_client(document.physical_path)
        try:
            blob_client.delete_blob()
            self._logger.info(f"Deleted blob {document.physical_path} for document {document.id}")
        except Exception as ex:
            # If blob does not exist, Azure SDK will raise an error — handle gracefully
            self._logger.warning(f"Failed to delete blob {document.physical_path}: {ex}")

        # Remove DB record (or mark physical_path None, depending on your design)
        deleted = self._document_repository.delete(document_id)
        return deleted


    # def _initialize_blob_client(self,storage_id:UUID):
    #     """
    #     Initializes BlobServiceClient + ContainerClient ONCE.
    #     """
    #     storage_type = self._storage_type_repository.get_by_id(storage_id)
    #     config = storage_type.configParam

    #     conn_str = self._build_connection_string(config)
    #     container_name = config.get("container_name", "documents")

    #     self.blob_service_client = BlobServiceClient.from_connection_string(conn_str)
    #     self.container_client = self.blob_service_client.get_container_client(container_name)

    #     # Ensure container exists
    #     try:
    #         self.container_client.create_container()
    #     except ResourceExistsError:
    #         pass


        
    def _build_connection_string(self,config: dict) -> str:
        """
        Build Azure connection string from configParam stored in DB.
        """
        return (
        f"DefaultEndpointsProtocol={config['DefaultEndpointsProtocol']};"
        f"AccountName={config['AccountName']};"
        f"AccountKey={config['AccountKey']};"
        f"BlobEndpoint={config['BlobEndpoint']};"
    )