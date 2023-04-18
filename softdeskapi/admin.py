from django.contrib import admin
from users.models import User
from softdeskapi.models import Contributor, Project, Issue, Comment


class UserAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'email')


class ContributorAdmin(admin.ModelAdmin):

    list_display = ('role',)


class ProjectAdmin(admin.ModelAdmin):

    list_display = ('title', 'description', 'type')


class IssueAdmin(admin.ModelAdmin):

    list_display = ('title', 'description', 'tag', 'priority', 'status')


class CommentAdmin(admin.ModelAdmin):

    list_display = ('description',)


admin.site.register(User, UserAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment, CommentAdmin)
