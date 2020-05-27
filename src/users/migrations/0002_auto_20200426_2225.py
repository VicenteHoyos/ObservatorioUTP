# Generated by Django 3.0.5 on 2020-04-27 03:25

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='biografia',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='ciudad',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='imagen_Perfil',
            field=models.ImageField(blank=True, null=True, upload_to=users.models.upload_location),
        ),
    ]
