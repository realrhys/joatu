# Generated by Django 2.0.3 on 2018-04-02 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0034_auto_20180330_1706'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project_attendees_registration',
            old_name='project',
            new_name='project_attendees',
        ),
        migrations.RenameField(
            model_name='project_volunteers_registration',
            old_name='project',
            new_name='project_volunteers',
        ),
        migrations.AddField(
            model_name='project_attendees_registration',
            name='project_attendees_ref',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project_volunteers_registration',
            name='project_volunteers_ref',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
