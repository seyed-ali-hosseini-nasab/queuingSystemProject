# Generated by Django 4.0.1 on 2022-01-06 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='is_evening_shift',
            field=models.BooleanField(default=True, verbose_name='Evening shift'),
        ),
    ]