from rest_framework import permissions
from rest_framework.permissions import BasePermission

from softdeskapi.models import Contributor, Project, Issue


class IsAdminAuthenticated(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)


class IsProjectContributor(BasePermission):

    message = "You are not a contributor to this project"

    def has_object_permission(self, request, view, obj):

        # all authenticated users can read and create a project
        if request.method in permissions.SAFE_METHODS:
            return True
        # obj.author_user == request.user or obj.project_contributor.filter(user_id=request.user.id)
        # only the author of the project can update or delete it
        return obj.author_user == request.user


class IsIssueAuthor(BasePermission):

    message = "You are neither a contributor to this project nor the author of this issue "

    def has_permission(self, request, view):

        if request.method == 'POST' or view.action == 'list':
            project = Project.objects.get(id=view.kwargs['project_pk'])
            contributors = Contributor.objects.filter(project=project)
            project_contributors = [contributor.user for contributor in contributors]
            return request.user == project.author_user or request.user in project_contributors
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        contributors = Contributor.objects.filter(project=obj.project)
        project_contributors = [contributor.user for contributor in contributors]

        if request.method in permissions.SAFE_METHODS:
            return request.user in project_contributors
        return request.user == obj.author_user or request.user == obj.project.author_user


class IsCommentAuthor(BasePermission):

    message = "You are neither a contributor to this project nor the author of this comment "

    def has_permission(self, request, view):

        if request.method == 'POST' or view.action == 'list':
            project = Project.objects.get(id=view.kwargs['project_pk'])
            issue = Issue.objects.get(id=view.kwargs['issue_pk'])
            return request.user == project.author_user or request.user == issue.author_user
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        contributors = Contributor.objects.filter(project=obj.issue.project)
        project_contributors = [contributor.user for contributor in contributors]

        # only project contributors (including the author of the project) can read and create a comment
        if request.method in permissions.SAFE_METHODS:
            return request.user in project_contributors

        # only the author of the comment can update or delete it
        return request.user == obj.author_user or request.user == obj.issue.project.author_user


class ContributorPermission(BasePermission):

    message = ""

    def has_permission(self, request, view):

        if request.method == 'POST' or view.action == 'list':
            project = Project.objects.get(id=view.kwargs['project_pk'])
            return request.user == project.author_user
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.project.author_user
