# Generated by Django 2.2.5 on 2020-04-29 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0017_uploadfilemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='boards'),
        ),
        migrations.AddField(
            model_name='board',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='boards'),
        ),
        migrations.RemoveField(
            model_name='board',
            name='photo',
        ),
        migrations.AddField(
            model_name='board',
            name='photo',
            field=models.ImageField(null=True, upload_to='boards'),
        ),
    ]
