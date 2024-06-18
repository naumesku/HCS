# Generated by Django 4.2.7 on 2024-06-13 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hcs', '0009_rename_mount_water_meter_month'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='water_meter',
            name='actual_tariff',
        ),
        migrations.RemoveField(
            model_name='water_meter',
            name='price',
        ),
        migrations.RemoveField(
            model_name='water_meter',
            name='volume',
        ),
        migrations.CreateModel(
            name='ServiceRendered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(choices=[('2023', '2023'), ('2024', '2024'), ('2025', '2025')], max_length=4, verbose_name='год')),
                ('month', models.CharField(choices=[('january', 'январь'), ('february', 'февраль'), ('march', 'март'), ('april', 'май'), ('may', 'май'), ('june', 'июнь'), ('july', 'июль'), ('august', 'август'), ('september', 'сентябрь'), ('october', 'октябрь'), ('ноябрь', 'November'), ('december', 'сентябрь')], max_length=10, verbose_name='месяц')),
                ('volume', models.FloatField(blank=True, null=True, verbose_name='объем воды за месяц')),
                ('actual_tariff_price', models.FloatField(blank=True, null=True, verbose_name='актуальный тариф на месяц')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='стоимость за объем')),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flat', to='hcs.flat')),
                ('tariff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tariff', to='hcs.tariff')),
            ],
            options={
                'verbose_name': 'Оказанная услуга',
                'verbose_name_plural': 'Оказанные услуги',
            },
        ),
    ]
