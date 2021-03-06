# Generated by Django 3.2.7 on 2021-09-28 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Centers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('dni_code', models.CharField(max_length=9)),
                ('cip_code', models.CharField(max_length=14)),
                ('birth_date', models.DateField(verbose_name='fecha nacimiento')),
                ('app_date', models.DateTimeField(verbose_name='fecha y hora visita')),
                ('center_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.centers')),
            ],
        ),
    ]
