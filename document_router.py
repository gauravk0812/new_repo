from typing import Optional
from uuid import UUID
from fastapi import APIRouter, File, HTTPException, UploadFile,status
from fastapi import Query
from fastapi.responses import StreamingResponse
from fastapi_injector import Injected
from fastapi_utils.cbv import cbv
from pylekhagaar.core.contracts.idocument_service import IDocumentService
from pylekhagaar.core.schemas.document import Document
from pycrud.core.data_filters.simple_search_filter import SimpleSearchFilter
from pycrud.core.schemas.paged_result import PagedResult
from pycrud.core.exceptions.not_found_exception import NotFoundException

document_router = APIRouter(prefix = "/documents")

@cbv(document_router)
class DocumentController:
    """ Controller for document related operations """
    def __init__(self, document_service: IDocumentService = Injected(IDocumentService)) -> None:
        self._document_service = document_service


    @document_router.get(path="/")
    def find(self, 
             search_text: Optional[str] = Query(None),
             sort_on: Optional[str] = Query(None),
             sort_ascending: bool = Query(True),
             page_index: int = Query(0),
             page_size: int = Query(10)
             ):
        """
        Find all documents.
        :return: A paged result containing a list of documents meta data.
        """

        # Create a SimpleSearchFilter instance with the provided parameters
        # and default values for search_text, sort_on, and sort_ascending
        data_filter = SimpleSearchFilter(search_text=search_text,
                                         sort_on=sort_on,
                                         sort_ascending=sort_ascending
                                         )
       
        # Call the service to find all students
        result: PagedResult[Document] = self._document_service.find(data_filter, page_index, page_size)
        return result
    


    @document_router.post(path="/", operation_id="create_document")
    def add(self, document: Document) -> Document:
        """
        Create a new document.
        :param document: Document object to be created.
        """
        
        # Call the service to add the student
        result: Document = self._document_service.add(document)
        return result
    

    @document_router.post("/{id}/content", operation_id="set_document_content")
    def set_document_content(self,id: UUID, file: UploadFile = File(...)):
        """
        Upload or replace file content for an existing document.
        - document_id: UUID of the document.
        - file: uploaded file stream.
        """
        try:
            updated_doc = self._document_service.set_document_content(id, file)
            return updated_doc
        except Exception as ex:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(ex)
        )



    @document_router.get("/{id}/document",operation_id="get_document_by_Id")
    def get_document(self,id: UUID) -> Document:
        """
        Get document metadata by ID.
        - document_id: UUID of the document.
        """
        try:
            document = self._document_service.get_by_id(id)
            return document
        except Exception as ex:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(ex)
        )


    @document_router.get("/{id}/content", operation_id="get_document_content")
    def get_document_content(self,id: UUID):
        """
            Download the file content of a document by ID.
            - document_id: UUID of the document.
            :return: StreamingResponse with the file content.
            """
        
        try:
            file_stream, filename = self._document_service.get_document_content(id)

            fileresponseData = StreamingResponse(
                                                file_stream,
                                                media_type="application/octet-stream",
                                                headers={"Content-Disposition": f'attachment; filename="{filename}"'}
                                                )
            return fileresponseData
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        

    @document_router.delete("/{id}/document", operation_id="delete_document")
    def delete_document(self,id: UUID):
        """
        Delete a document by ID.
        - document_id: UUID of the document.
        """
        
        try:
            self._document_service.delete_document(id)
            return {"message": f"Document {id} deleted successfully"}
        except NotFoundException as e:
            raise HTTPException(status_code=404, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))