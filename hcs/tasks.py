from celery import shared_task
from hcs.serializers import *
from datetime import datetime


@shared_task
def calculat_pait_wather(pk):
    """
    Отложенная функция расчета стоимости
    Поринимает pk созданного показания счетчика
    Расчитывает квартплату на основании актуальных данных счетчика и тарифа.
    """

    # созданная только что сущность
    now_water_meter = Water_Meter.objects.filter(pk=pk).first()

    # находим прошлые показания счетчика с заданным подогревом
    water_meters = Water_Meter.objects.filter(is_hot=now_water_meter.is_hot).order_by("-date").all()

    if water_meters.count() > 1:
        last_water_meter = water_meters[1].data_meter
    else:
        last_water_meter = 0

    # находим объем использованной воды.
    volume = now_water_meter.data_meter - last_water_meter

    # находим актуальную стоимоть услуги по тарифу
    if now_water_meter.is_hot:
        actual_tariff = Tariff.objects.filter(
           service_name=Tariff.ServiceChoice.RASE_WATER_HOT
        ).order_by("-date").first()

    else:
        actual_tariff = Tariff.objects.filter(
            service_name=Tariff.ServiceChoice.RASE_WATER_COLD
        ).order_by("-date").first()

    price_actual_tariff = actual_tariff.price_per_unit

    if volume < 0:
        volume = 0

    prise = round((price_actual_tariff * volume), 2)

    # Сохраняем в БД новые данные
    data = {
        "flat": now_water_meter.flat.id,
        "tariff": actual_tariff.id,
        "volume": round(volume, 2),
        "price": prise,
    }

    serializer = ServiceRenderedSerializer
    serializer_instance = serializer(data=data)
    if serializer_instance.is_valid():
        serializer_instance.save()

@shared_task
def calculat_pait_keep_prop():
    """Периодическая функция расчета стоимости кварплдаты за хранение имущества"""
    print("задача запущена")
    month_now = datetime.now().month
    actual_tariff = Tariff.objects.filter(service_name=Tariff.ServiceChoice.KEEP_PROPERTY).order_by("-date").first()

    # Формируем список id всех квартир
    all_flats_id = set([flat.id for flat in Flat.objects.all()])

    # Формируем список уже расчитанных услуг
    service_get = ServiceRendered.objects.filter(
        date__month=month_now,
        tariff=actual_tariff,
        )

    # Формируем множество уже расчитанных квартир
    flat_keep_id = set(service.flat.id for service in service_get)

    # Формируем список квартир с нерасчитанной услугой
    flat_not_keep_id = list(all_flats_id.difference(flat_keep_id))

    # Расчитываем и записываем в модель услуг стоимость хранения имущества для подготовленных квартир
    if actual_tariff:
        for flat_id in flat_not_keep_id:
            flat = Flat.objects.filter(id=flat_id).first()
            price = round((flat.area * actual_tariff.price_per_unit), 2)

            data = {
                "flat": flat.id,
                "tariff": actual_tariff.id,
                "price": price,
            }

            serializer = ServiceRenderedSerializer
            serializer_instance = serializer(data=data)
            if serializer_instance.is_valid():
                serializer_instance.save()
    else:
        print("Нет тарифа для содержание общего имущества")
