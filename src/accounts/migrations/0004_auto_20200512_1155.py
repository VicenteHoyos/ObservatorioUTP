# Generated by Django 2.2.6 on 2020-05-12 16:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_auto_20170211_1038'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Follower',
        ),
    ]
