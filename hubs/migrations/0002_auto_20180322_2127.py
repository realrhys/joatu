# Generated by Django 2.0.3 on 2018-03-23 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hubs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HubGeolocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.CharField(blank=True, max_length=30, null=True)),
                ('lng', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='HubInfo',
            new_name='Hub',
        ),
        migrations.AddField(
            model_name='hubgeolocation',
            name='hub',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hubs.Hub'),
        ),
    ]
