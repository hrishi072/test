# Generated by Django 3.2.5 on 2021-07-23 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_userprofile_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='date',
        ),
    ]