# Generated by Django 4.2.7 on 2024-06-13 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hcs', '0010_remove_water_meter_actual_tariff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerendered',
            name='month',
            field=models.CharField(max_length=10, verbose_name='месяц'),
        ),
        migrations.AlterField(
            model_name='servicerendered',
            name='year',
            field=models.CharField(max_length=4, verbose_name='год'),
        ),
    ]