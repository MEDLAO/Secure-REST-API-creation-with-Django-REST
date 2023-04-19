from rest_framework.serializers import ModelSerializer
from users.models import User
from softdeskapi.models import Contributor, Project, Issue, Comment


class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ContributorsSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = "__all__"


class ProjectsSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class IssuesSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"


class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
