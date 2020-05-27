# Generated by Django 3.0.5 on 2020-05-02 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_interes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interes',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.RemoveField(
            model_name='post',
            name='interes',
        ),
        migrations.AddField(
            model_name='post',
            name='interes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='posts.Interes'),
            preserve_default=False,
        ),
    ]
