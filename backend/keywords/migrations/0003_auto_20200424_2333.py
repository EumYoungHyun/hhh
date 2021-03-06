# Generated by Django 2.2.5 on 2020-04-24 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('keywords', '0002_auto_20200408_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Location'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.DiningStore'),
        ),
    ]
