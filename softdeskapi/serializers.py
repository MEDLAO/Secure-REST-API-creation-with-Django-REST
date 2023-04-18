from rest_framework.serializers import ModelSerializer
from users.models import Users
from softdeskapi.models import Contributors, Projects, Issues, Comments


class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class ContributorsSerializer(ModelSerializer):
    class Meta:
        model = Contributors
        fields = "__all__"


class ProjectsSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"


class IssuesSerializer(ModelSerializer):
    class Meta:
        model = Issues
        fields = "__all__"


class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"
