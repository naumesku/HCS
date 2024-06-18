# Generated by Django 4.2.7 on 2024-06-15 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hcs', '0013_alter_servicerendered_date_alter_tariff_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerendered',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='стоимость за объем'),
        ),
        migrations.AlterField(
            model_name='servicerendered',
            name='volume',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='объем воды за месяц'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='price_per_unit',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='цена за единицу'),
        ),
    ]