from django.db.models import Q
from rest_framework.permissions import BasePermission

from workspaces.models import Workspace


class IsActionWorkspaceManager(BasePermission):
    """Custom permission to only allow managers of a workspace to view or edit
    actions within it.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        if not obj.workspace:
            return True

        return Workspace.objects.filter(
            Q(pk=obj.workspace.id),
            Q(users_managers=user)
            | Q(groups_managers__user_set=user)
            | Q(roles_managers__users=user)
            | Q(roles_managers__groups__user_set=user),
        ).exists()


class IsActionWorkspaceMember(BasePermission):
    """Custom permission to only allow members of a workspace to view actions
    within it.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        if not obj.workspace:
            return True

        return Workspace.objects.filter(
            Q(pk=obj.workspace.id),
            Q(actions_allowed_users=user)
            | Q(actions_allowed_groups__user_set=user)
            | Q(actions_allowed_roles__users=user)
            | Q(actions_allowed_roles__groups__user_set=user),
        ).exists()
