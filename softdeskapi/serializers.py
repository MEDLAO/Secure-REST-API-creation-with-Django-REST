from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from softdeskapi.models import Contributor, Project, Issue, Comment
from users.serializers import UserSerializer


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


class IssueListSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ['title', 'description', 'tag', 'priority', 'status', 'author_user_id', 'assigned_user_id', 'created_time', 'comments']


class IssueDetailSerializer(ModelSerializer):

    comments = CommentSerializer

    class Meta:
        model = Issue
        fields = ['title', 'description', 'project_id', 'tag', 'priority', 'status', 'author_user_id', 'assigned_user_id', 'created_time', 'comments']


class ProjectListSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['title', 'description', 'type', 'author_user_id', 'issues']


class ProjectDetailSerializer(ModelSerializer):

    issues = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['title', 'description', 'type', 'author_user_id', 'issues']

    def get_issues(self, instance):
        queryset = instance.issues.all()
        serializer = IssueListSerializer(queryset, many=True)
        return serializer.data


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['id', 'user_id', 'project_id', 'role']
