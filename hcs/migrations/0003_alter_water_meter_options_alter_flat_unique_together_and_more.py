# Generated by Django 4.2.7 on 2024-06-12 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hcs', '0002_alter_home_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='water_meter',
            options={'verbose_name': 'Счетчик воды', 'verbose_name_plural': 'Счетчики воды'},
        ),
        migrations.AlterUniqueTogether(
            name='flat',
            unique_together={('home', 'flat_number')},
        ),
        migrations.AlterUniqueTogether(
            name='tariff',
            unique_together={('service_name', 'price_per_unit', 'unit_of_measure')},
        ),
    ]
