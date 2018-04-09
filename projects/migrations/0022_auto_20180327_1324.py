# Generated by Django 2.0.3 on 2018-03-27 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_auto_20180327_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_volunteers',
            name='project',
        ),
        migrations.AddField(
            model_name='project_volunteers',
            name='project',
            field=models.ManyToManyField(related_name='volunteers', to='projects.Project'),
        ),
    ]
