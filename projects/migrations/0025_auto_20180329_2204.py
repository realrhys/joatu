# Generated by Django 2.0.3 on 2018-03-30 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0024_auto_20180329_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_attendees',
            name='seats',
            field=models.PositiveSmallIntegerField(default=2, null=True),
        ),
    ]
