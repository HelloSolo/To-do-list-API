# Generated by Django 4.0.5 on 2022-07-01 11:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='List',
            new_name='UserList',
        ),
    ]
