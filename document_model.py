from typing import Optional
import uuid
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from pycrud.models.base_tenant_model import BaseTenantModel
from sqlalchemy.dialects.postgresql import UUID


class DocumentModel(BaseTenantModel):
    """
    Document model that extends BaseModel for resource-related database models.
    """

    __tablename__ = "document_detail"

    name: Mapped[Optional[str]] = mapped_column(String(1000), nullable=True)
    description: Mapped[Optional[str]] = mapped_column(String(2000), nullable=True)
    mime_type: Mapped[Optional[str]] = mapped_column(String(1000), nullable=True)
    physical_path: Mapped[Optional[str]] = mapped_column(String(1000), nullable=True)
    author: Mapped[Optional[str]] = mapped_column(String(1000), nullable=True)
    doc_type: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    storage_type: Mapped[Optional[str]] = mapped_column(String(500),default="filesystem", nullable=True)
    storage_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid = True), nullable = True)


    def must_implement(self) -> None:
        pass
