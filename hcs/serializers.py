from rest_framework import serializers
from hcs.models import *


class FlatSerializer(serializers.ModelSerializer):
    """Сериализатор для квартиры"""

    class Meta:
        model = Flat
        fields = '__all__'


class HouseSerializer(serializers.ModelSerializer):
    """Сериализатор для дома"""
    flat = FlatSerializer(source='flat_set', many=True, read_only=True)

    class Meta:
        model = House
        fields = '__all__'


class Water_MeterSerializer(serializers.ModelSerializer):
    """Сериализатор для счетчика воды"""

    def __init__(self, *args, **kwargs):
        super(Water_MeterSerializer, self).__init__(*args, **kwargs)
        for field_name in ['volume', 'actual_tariff', 'actual_price',]:
            self.fields.pop(field_name, None)

    class Meta:
        model = Water_Meter
        fields = '__all__'


class TariffSerializer(serializers.ModelSerializer):
    """Сериализатор для дома"""

    class Meta:
        model = Tariff
        fields = '__all__'


class ServiceRenderedSerializer(serializers.ModelSerializer):
    """Сериализатор для услуги"""

    class Meta:
        model = ServiceRendered
        fields = '__all__'

