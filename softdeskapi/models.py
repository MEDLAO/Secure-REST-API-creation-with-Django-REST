from django.db import models


class Contributors(models.Model):

    AUTHOR = 'AUTHOR'
    CONTRIBUTOR = 'CONTRIBUTOR'

    ROLE_CHOICES = ((AUTHOR, 'Auteur'), (CONTRIBUTOR, 'Contributeur'),)

    user_id = models.ForeignKey('users.Users', on_delete=models.CASCADE, related_name='contributor-user')
    project_id = models.ForeignKey('softdeskapi.Projects', on_delete=models.CASCADE, related_name='contributor-project')
    role = models.CharField(max_length=128, choices=ROLE_CHOICES, verbose_name='Rôle')


class Projects(models.Model):

    def __str__(self):
        return self.title

    class Type(models.TextChoices):
        BACK_END = 'Back-End'
        FRONT_END = 'Front-End'
        IOS = 'iOS'
        ANDROID = 'Android'

    project_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=5000)
    type = models.CharField(choices=Type.choices, max_length=10)
    author_user_id = models.ForeignKey('users.Users', on_delete=models.CASCADE)


class Issues(models.Model):

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

    issue_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=5000)
    tag = models.CharField(choices=Tag.choices, max_length=15)
    priority = models.CharField(choices=Priority.choices, max_length=10)
    status = models.CharField(choices=Status.choices, max_length=15)
    author_user_id = models.ForeignKey('users.Users', on_delete=models.CASCADE, related_name='issue-author')
    assignee_user_id = models.ForeignKey('users.Users', on_delete=models.CASCADE, default=issue_id, related_name='issue-assignee')
    created_time = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=5000)
    author_user_id = models.ForeignKey('users.Users', on_delete=models.CASCADE, related_name='comment-author')
    issue_id = models.ForeignKey('softdeskapi.Users', on_delete=models.CASCADE, related='comment-issue')
