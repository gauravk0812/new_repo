from typing import Optional, List

from pylekhagaar.core.contracts.idocument_permission_checker import IDocumentPermissionChecker


class DocumentPermissionCheckerImpl(IDocumentPermissionChecker):
    """
    This class implements the IStudentPermissionChecker interface.
    It provides methods to ensure that the current user has the required permissions
    for performing actions on student data.
    """

    def ensure_permissions(
        self,
        all_of_permissions: Optional[List[str]] = None,
        any_of_permissions: Optional[List[str]] = None,
    ) -> None:
        
        """
        Ensures that the current user has the required permissions.
        :param all_of_permissions: A list of permissions that the user must have.
        :param any_of_permissions: A list of permissions where at least one must be held by the user.
        :raises PermissionDenied: If the user does not have the required permissions.
        """
        
        pass