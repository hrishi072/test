# Generated by Django 3.2.5 on 2021-07-23 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app1', '0003_remove_userprofile_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('no', models.IntegerField(max_length=10)),
                ('userprofile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.userprofile')),
            ],
        ),
    ]
