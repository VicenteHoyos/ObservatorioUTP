# Generated by Django 3.0.5 on 2020-05-02 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20200502_0142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='interes',
        ),
        migrations.AddField(
            model_name='post',
            name='interes',
            field=models.ManyToManyField(to='posts.Interes'),
        ),
    ]
