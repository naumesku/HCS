from rest_framework import viewsets, generics
from hcs.tasks import *


class HouseViewSet(viewsets.ModelViewSet):
    """Представление для модели Дом"""
    serializer_class = HouseSerializer
    queryset = House.objects.all()


class FlatViewSet(viewsets.ModelViewSet):
    """Представление для модели Квартира"""
    serializer_class = FlatSerializer
    queryset = Flat.objects.all()


class WaterMeterViewSet(viewsets.ModelViewSet):
    """Представление для модели Счетчик Воды"""
    serializer_class = Water_MeterSerializer
    queryset = Water_Meter.objects.all()

    def perform_create(self, serializer):
        """
        Переопределяем метод крейт,
        добавляя отложенную функцйию заполнения таблицы по услугам
        """
        now_water_meter = serializer.save()
        calculat_pait_wather.delay(now_water_meter.pk)


class TariffViewSet(viewsets.ModelViewSet):
    """Представление для модели Трафик"""
    serializer_class = TariffSerializer
    queryset = Tariff.objects.all()


class ServiceRenderedCreateAPIView(generics.CreateAPIView):
    """Представление для создания услуги"""
    serializer_class = ServiceRenderedSerializer


class ServiceRenderedDestroyAPIView(generics.DestroyAPIView):
    """Представление для удаления услуги"""
    serializer_class = ServiceRenderedSerializer


class ServiceRenderedRetrieveAPIView(generics.RetrieveAPIView):
    """Представление для редактирования услуги"""
    serializer_class = ServiceRenderedSerializer


class ServiceRenderedListAPIView(generics.ListAPIView):
    """Представление для запроса данных об услагах в квартирах на основве ввода №дома и месяца."""
    serializer_class = ServiceRenderedSerializer

    def get_queryset(self):

        house_number = self.request.query_params.get('house_number')
        month = self.request.query_params.get('month')
        print("house_number=", house_number)
        print("month=", month)

        if house_number and month:
            # Фильтрация квартир по номеру дома и месяцу услуг
            service = ServiceRendered.objects.filter(
                flat__house__house_number=house_number,
                date__month=month
            )
        else:
            service = ({"error": "Необходимо верно указать номер дома и месяц."})
        return service
