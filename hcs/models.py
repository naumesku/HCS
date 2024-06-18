from django.db import models
from rest_framework.exceptions import ValidationError
from config.settings import NULLABLE


class House(models.Model):
    """Модель дома"""

    house_number = models.PositiveIntegerField(verbose_name="номер дома")
    town = models.CharField(max_length=30, verbose_name="город")
    street = models.TextField(max_length=100, verbose_name="улица")

    def __str__(self):
        return f'{self.street} - {self.house_number}'

    class Meta:
        unique_together = ('town', 'street', 'house_number')
        verbose_name = "дом"
        verbose_name_plural = "дома"


class Flat(models.Model):
    """Модель кваритиры"""

    house = models.ForeignKey(House, on_delete=models.CASCADE, verbose_name="номер дома")
    flat_number = models.PositiveIntegerField(verbose_name="номер квартиры")
    area = models.FloatField(verbose_name="площадь квартиры")

    def __str__(self):
        return f'{self.flat_number}'

    class Meta:
        unique_together = ('house', 'flat_number')
        verbose_name = "квартира"
        verbose_name_plural = "квартиры"


class Water_Meter(models.Model):
    """Модель счетчика воды"""

    serial_number = models.PositiveIntegerField(verbose_name="серийный номер")
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, verbose_name="номер квартира")
    is_hot = models.BooleanField(default=False, verbose_name="подогрев воды")
    data_meter = models.FloatField(verbose_name="данные счетчика в текущем месяце")
    date = models.DateTimeField(auto_now_add=True, verbose_name="дата и время показаний", **NULLABLE)

    class Meta:
        verbose_name = 'Счетчик воды'
        verbose_name_plural = 'Счетчики воды'

    def __str__(self):
        return f'Квартира{self.flat} - S/N счетчика{self.serial_number}'


class Tariff(models.Model):
    """Модель тарифа"""

    class ServiceChoice(models.TextChoices):
        """Класс для выбора услуги"""

        RASE_WATER_COLD = 'Стоимость 1м3 холодной воды', 'Стоимость 1м3 холодной воды'
        RASE_WATER_HOT = 'Стоимость 1м3 горячей воды', 'Стоимость 1м3 горячей воды'
        KEEP_PROPERTY = 'Содержание общего имущества за 1м2', 'Содержание общего имущества за 1м2'

    service_name = models.CharField(max_length=255, choices=ServiceChoice.choices, verbose_name='название услуги')
    price_per_unit = models.FloatField(verbose_name='цена за единицу')
    date = models.DateTimeField(auto_now_add=True, verbose_name="дата создания тарифа", **NULLABLE)

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

    def __str__(self):
        return f'{self.service_name} - {self.price_per_unit}'

    def save(self, *args, **kwargs):
        """Проверка на дубль тарифов за один и тот же период"""
        if Tariff.objects.filter(
                service_name=self.service_name,
                price_per_unit=self.price_per_unit,
        ).exists():
            raise ValidationError("Данные уже внесены, но вы можете их изменить")
        super().save(*args, **kwargs)

class ServiceRendered(models.Model):
    """Модель оказанных услуг"""

    date = models.DateTimeField(auto_now_add=True, verbose_name="дата и время формирования услуги", **NULLABLE)
    flat = models.ForeignKey('Flat', on_delete=models.CASCADE, related_name='flat')
    tariff = models.ForeignKey('Tariff', on_delete=models.CASCADE, related_name='tariff')
    volume = models.FloatField(verbose_name="объем воды за месяц", **NULLABLE)
    price = models.FloatField(verbose_name="стоимость за объем", **NULLABLE)

    class Meta:
        verbose_name = 'Оказанная услуга'
        verbose_name_plural = 'Оказанные услуги'

    def __str__(self):
        return f'{self.flat} - {self.price}'
