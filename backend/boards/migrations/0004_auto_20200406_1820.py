# Generated by Django 2.2.5 on 2020-04-06 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_auto_20200406_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='board',
        ),
        migrations.AddField(
            model_name='board',
            name='like',
            field=models.ManyToManyField(to='boards.Like'),
        ),
        migrations.AddField(
            model_name='board',
            name='photo',
            field=models.ManyToManyField(to='boards.Photo'),
        ),
    ]
