from rest_framework.exceptions import NotAcceptable
from rest_framework.viewsets import ModelViewSet
from softdeskapi.models import Project, Issue, Comment, Contributor
from softdeskapi.serializers import ProjectDetailSerializer, ProjectListSerializer, CommentSerializer, \
    IssueListSerializer, IssueDetailSerializer, ContributorSerializer
from users.models import User
from users.serializers import UserSerializer


class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProjectViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ProjectListSerializer  # default serializer
    detail_serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        return Project.objects.all()


class IssueViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer

    def get_queryset(self):
        return Issue.objects.filter(project_id_id=self.kwargs['project_pk'])
        # return Issue.objects.all()

    def perform_create(self, serializer):
        project = Project.objects.get(id=self.kwargs['project_pk'])
        serializer.save(project_id=project)

    def get_object(self):
        try:
            issue = Issue.objects.get(id=int(self.kwargs['pk']))
            if issue.project_id.pk != self.kwargs['project_pk']:
                raise NotAcceptable("This issue doesn't belong to this project")
            return issue
        except Exception as e:
            raise NotAcceptable(str(e))


class CommentViewset(ModelViewSet):

    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(issue_id_id=self.kwargs['issue_pk'])
        # return Comment.objects.all()

    def get_object(self):
        try:
            comment = Comment.objects.get(id=int(self.kwargs['pk']))
            if comment.issue_id.pk != self.kwargs['issue_pk']:
                raise NotAcceptable("This comment is not attached to this issue")
            return comment
        except Exception as e:
            raise NotAcceptable(str(e))


class ContributorViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ContributorSerializer

    def get_queryset(self):
        project = Project.objects.get(id=self.kwargs['project_pk'])
        return Contributor.objects.filter(project_id=project)


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
