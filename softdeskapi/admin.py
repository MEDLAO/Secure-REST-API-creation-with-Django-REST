from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User
from softdeskapi.models import Contributor, Project, Issue, Comment
from users.forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("email", "is_staff", "is_active", "first_name", "last_name")
    list_filter = ("email", "is_staff", "is_active", "first_name", "last_name")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


class UserAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'email')


class ContributorAdmin(admin.ModelAdmin):

    list_display = ('user_id', 'project_id', 'role',)


class ProjectAdmin(admin.ModelAdmin):

    list_display = ('title', 'description', 'type')


class IssueAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'description', 'project_id', 'tag', 'priority', 'status')


class CommentAdmin(admin.ModelAdmin):

    list_display = ('id','description','author_user_id', 'issue_id')


admin.site.register(User, CustomUserAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment, CommentAdmin)
