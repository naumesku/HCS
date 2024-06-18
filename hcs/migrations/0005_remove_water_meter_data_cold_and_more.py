# Generated by Django 4.2.7 on 2024-06-12 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hcs', '0004_rename_float_number_water_meter_flat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='water_meter',
            name='data_cold',
        ),
        migrations.RemoveField(
            model_name='water_meter',
            name='data_hot',
        ),
        migrations.AddField(
            model_name='water_meter',
            name='data',
            field=models.FloatField(blank=True, null=True, verbose_name='количество м3 за месяц'),
        ),
        migrations.AddField(
            model_name='water_meter',
            name='is_hot',
            field=models.BooleanField(default=False, verbose_name='подогрев воды'),
        ),
    ]
