# Generated by Django 4.2 on 2023-04-19 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('AUTHOR', 'Auteur'), ('CONTRIBUTOR', 'Contributeur')], max_length=128, verbose_name='Rôle')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=5000)),
                ('tag', models.CharField(choices=[('Bug', 'Bug'), ('Amélioration', 'Improvement'), ('Tâche', 'Task')], max_length=15)),
                ('priority', models.CharField(choices=[('Faible', 'Low'), ('Moyenne', 'Medium'), ('Élevée', 'High')], max_length=10)),
                ('status', models.CharField(choices=[('À faire', 'To Do'), ('En cours', 'In Progress'), ('Terminé', 'Completed')], max_length=15)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=5000)),
                ('type', models.CharField(choices=[('Back-End', 'Back End'), ('Front-End', 'Front End'), ('iOS', 'Ios'), ('Android', 'Android')], max_length=10)),
            ],
        ),
    ]
