# Generated by Django 4.1 on 2024-04-26 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fasosapp', '0004_rename_jenis_localgovernmentoffice_tipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localgovernmentoffice',
            name='nama',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='medicalfacility',
            name='nama',
            field=models.CharField(max_length=150),
        ),
    ]