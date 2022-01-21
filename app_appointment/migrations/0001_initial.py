# Generated by Django 4.0.1 on 2022-01-06 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_hospital', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turn_number', models.IntegerField(verbose_name='Turn number')),
                ('shift', models.CharField(max_length=30, verbose_name='Shift')),
                ('shift_en', models.CharField(max_length=30, null=True, verbose_name='Shift')),
                ('shift_fa', models.CharField(max_length=30, null=True, verbose_name='Shift')),
                ('visiting_hours', models.CharField(max_length=10, verbose_name='Visiting hours')),
                ('date', models.DateField(verbose_name='Date')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_hospital.doctor', verbose_name='Doctor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Appointment',
                'verbose_name_plural': 'Appointments',
            },
        ),
    ]