# Generated by Django 3.0.5 on 2020-05-03 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_auto_20200502_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categorias',
            field=models.ManyToManyField(related_name='get_posts', to='posts.Interes', verbose_name='Categorías'),
        ),
    ]
