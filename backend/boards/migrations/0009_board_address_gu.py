# Generated by Django 2.2.5 on 2020-04-24 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0008_auto_20200422_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='address_gu',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
