from rest_framework.exceptions import NotAcceptable
from rest_framework.viewsets import ModelViewSet
from softdeskapi.models import Project, Issue, Comment, Contributor
from softdeskapi.permissions import IsProjectContributor, IsCommentAuthor, IsIssueAuthor, ContributorPermission
from softdeskapi.serializers import ProjectDetailSerializer, ProjectListSerializer, CommentSerializer, \
    IssueListSerializer, IssueDetailSerializer, ContributorSerializer
from users.models import User
from users.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated


class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'create' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProjectViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ProjectListSerializer  # default serializer
    detail_serializer_class = ProjectDetailSerializer
    permission_classes = [IsAuthenticated, IsProjectContributor]

    def get_queryset(self):
        connected_user_contributors = Contributor.objects.filter(user=self.request.user)
        connected_user_projects = [contributor.project.id for contributor in connected_user_contributors]
        return Project.objects.filter(id__in=connected_user_projects)

    def create(self, request, *args, **kwargs):
        obj = super().create(request, *args, **kwargs)
        project_id = obj.data['id']
        author_user_id = obj.data['author_user']
        project = Project.objects.get(id=project_id)
        author_user = User.objects.get(id=author_user_id)
        Contributor.objects.create(project=project, user=author_user, role=Contributor.AUTHOR)
        return obj


class IssueViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer
    permission_classes = [IsAuthenticated, IsIssueAuthor]

    def get_queryset(self):
        return Issue.objects.filter(project_id=self.kwargs['project_pk'])
        # return Issue.objects.all()

    def perform_create(self, serializer):
        project = Project.objects.get(id=self.kwargs['project_pk'])
        serializer.save(project=project)

    def get_object(self):
        try:
            issue = Issue.objects.get(id=int(self.kwargs['pk']))
            self.check_object_permissions(self.request, issue)
            if issue.project.pk != self.kwargs['project_pk']:
                raise NotAcceptable("This issue doesn't belong to this project")
            return issue
        except Exception as e:
            raise NotAcceptable(str(e))


class CommentViewset(ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsCommentAuthor]

    def get_queryset(self):
        return Comment.objects.filter(issue_id=self.kwargs['issue_pk'])
        # return Comment.objects.all()

    def get_object(self):
        try:
            comment = Comment.objects.get(id=int(self.kwargs['pk']))
            self.check_object_permissions(self.request, comment)
            if comment.issue.pk != self.kwargs['issue_pk']:
                raise NotAcceptable("This comment is not attached to this issue")
            return comment
        except Exception as e:
            raise NotAcceptable(str(e))


class ContributorViewset(ModelViewSet):

    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, ContributorPermission]

    def get_queryset(self):
        project = Project.objects.get(id=self.kwargs['project_pk'])
        return Contributor.objects.filter(project=project)


    # def get_queryset(self):
    #     all_contributors = Contributor.objects.filter(project_id=self.kwargs['project_pk'])
    #     users_contributors = [contributor.user_id for contributor in all_contributors]
    #     all_ids = [user.id for user in users_contributors]
    #     unique_users_contributors = User.objects.filter(id__in=all_ids)
    #     return unique_users_contributors
    #
    # def perform_create(self, serializer):
    #     user = serializer.save()
    #     project = Project.objects.get(id=self.kwargs['project_pk'])
    #     Contributor.objects.create(user_id=user, project_id=project)
    #
    # def get_object(self):
    #     try:
    #         user = User.objects.get(id=int(self.kwargs['pk']))
    #         contributor = Contributor.objects.get(user_id=user)
    #         if contributor.project_id.pk != self.kwargs['project_pk']:
    #             raise NotAcceptable("This user is not attached to this project")
    #         return user
    #     except Exception as e:
    #         raise NotAcceptable(str(e))
