# Generated by Django 3.0.5 on 2020-04-28 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200427_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='biografia',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='ciudad',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='telefono',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
