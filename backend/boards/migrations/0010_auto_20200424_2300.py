# Generated by Django 2.2.5 on 2020-04-24 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0009_board_address_gu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, to='boards.Like'),
        ),
    ]
