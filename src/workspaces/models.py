from django.db import models

from users.models import User


class Workspace(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="workspaces_created",
        blank=True,
        null=True,
    )
    users_managers = models.ManyToManyField(
        User,
        related_name="workspaces_users_managed",
        blank=True,
    )
    groups_managers = models.ManyToManyField(
        "users.Group",
        related_name="workspaces_groups_managed",
        blank=True,
    )
    roles_managers = models.ManyToManyField(
        "users.Role",
        related_name="workspaces_roles_managed",
        blank=True,
    )
    actions_allowed_users = models.ManyToManyField(
        User,
        related_name="workspaces_actions_allowed_users",
        blank=True,
    )
    actions_allowed_groups = models.ManyToManyField(
        "users.Group",
        related_name="workspaces_actions_allowed_groups",
        blank=True,
    )
    actions_allowed_roles = models.ManyToManyField(
        "users.Role",
        related_name="workspaces_actions_allowed_roles",
        blank=True,
    )
