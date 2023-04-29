# Generated by Django 4.2 on 2023-04-23 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('softdeskapi', '0004_alter_issue_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_contributor', to='softdeskapi.project'),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_contributor', to=settings.AUTH_USER_MODEL),
        ),
    ]