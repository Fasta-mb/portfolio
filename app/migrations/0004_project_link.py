# Generated by Django 4.1.5 on 2023-01-13 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_profile_project_profile_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
    ]
