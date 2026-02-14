from rest_framework import serializers

from users.models import Group, Role, User
from users.serializers.group_serializers import GroupDetailedSerializer
from users.serializers.role_serializers import RoleDetailedSerializer
from users.serializers.user_serializers import ShortUserSerializer

from .models import Workspace


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = [
            "id",
            "name",
            "description",
            "created_at",
            "updated_at",
            "is_active",
        ]

    def create(self, validated_data):
        validated_data["created_by"] = self.context["request"].user
        return super().create(validated_data)


class DetailedWorkspaceSerializer(WorkspaceSerializer):
    created_by = ShortUserSerializer(read_only=True)
    users_managers = ShortUserSerializer(many=True, read_only=True)
    users_managers_ids = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        many=True,
        write_only=True,
        source="users_managers",
    )
    groups_managers = GroupDetailedSerializer(many=True, read_only=True)
    groups_managers_ids = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(),
        many=True,
        write_only=True,
        source="groups_managers",
    )
    roles_managers = RoleDetailedSerializer(many=True, read_only=True)
    roles_managers_ids = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(),
        many=True,
        write_only=True,
        source="roles_managers",
    )

    class Meta(WorkspaceSerializer.Meta):
        fields = WorkspaceSerializer.Meta.fields + [
            "created_by",
            "users_managers",
            "groups_managers",
            "roles_managers",
            "users_managers_ids",
            "groups_managers_ids",
            "roles_managers_ids",
        ]
