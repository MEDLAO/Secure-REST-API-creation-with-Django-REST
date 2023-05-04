# Generated by Django 4.2 on 2023-04-29 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('softdeskapi', '0007_alter_contributor_project_id_and_more'),
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