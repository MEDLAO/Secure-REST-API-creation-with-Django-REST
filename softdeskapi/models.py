from django.conf import settings
from django.db import models


class Project(models.Model):

    def __str__(self):
        return str(self.id) + " - " + self.title

    class Type(models.TextChoices):
        BACK_END = 'Back-End'
        FRONT_END = 'Front-End'
        IOS = 'iOS'
        ANDROID = 'Android'

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=5000)
    type = models.CharField(choices=Type.choices, max_length=10)
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Contributor(models.Model):

    AUTHOR = 'AUTHOR'
    CONTRIBUTOR = 'CONTRIBUTOR'

    ROLE_CHOICES = ((AUTHOR, 'Auteur'), (CONTRIBUTOR, 'Contributeur'),)

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_contributor')
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='project_contributor')
    role = models.CharField(max_length=128, choices=ROLE_CHOICES, verbose_name='Rôle')

    class Meta:

        unique_together = ('user', 'project',)


class Issue(models.Model):

    def __str__(self):
        return self.title

    class Tag(models.TextChoices):
        BUG = 'Bug'
        IMPROVEMENT = 'Amélioration'
        TASK = 'Tâche'

    class Priority(models.TextChoices):
        LOW = 'Faible'
        MEDIUM = 'Moyenne'
        HIGH = 'Élevée'

    class Status(models.TextChoices):
        TO_DO = 'À faire'
        IN_PROGRESS = 'En cours'
        COMPLETED = 'Terminé'

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=5000)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, null=True, related_name='issues')
    tag = models.CharField(choices=Tag.choices, max_length=15)
    priority = models.CharField(choices=Priority.choices, max_length=10)
    status = models.CharField(choices=Status.choices, max_length=15)
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='issue_author')
    assigned_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='issue_assigned')
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):

    description = models.CharField(max_length=5000)
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE, related_name='comments')
