# Generated by Django 3.2.5 on 2021-07-23 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_userprofile_date'),
        ('app2', '0002_alter_userdata_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='userprofile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.userprofile'),
        ),
    ]
