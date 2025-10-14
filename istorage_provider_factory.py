
from abc import ABC
import uuid
from pylekhagaar.core.contracts.istorage_provider import IStorageProvider


class IStorageProviderFactory(ABC):
    def get_storage_provider(self, storage_id: uuid.UUID) -> IStorageProvider:
        """ Get the appropriate storage provider based on the storage type.
        :param storage_type: Type of storage (e.g., 'azure_blob', 'local_file_system').
        :return: An instance of IStorageProvider.
        """
        pass