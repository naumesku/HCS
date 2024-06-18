from django.urls import path
from rest_framework.routers import DefaultRouter
from hcs.apps import HcsConfig
from hcs.views import *


app_name = HcsConfig.name

router_house = DefaultRouter()
router_house.register(r'house', HouseViewSet, basename='house')

router_flat = DefaultRouter()
router_flat.register(r'flat', FlatViewSet, basename='flat')

router_water_meter = DefaultRouter()
router_water_meter.register(r'water_meter', WaterMeterViewSet, basename='water_meter')

router_tariff = DefaultRouter()
router_tariff.register(r'tariff', TariffViewSet, basename='tariff')

urlpatterns = [
    path('service/create/', ServiceRenderedCreateAPIView.as_view(), name='service-create'),
    path('service/', ServiceRenderedListAPIView.as_view(), name='service-list'),
    path('service/delete/', ServiceRenderedDestroyAPIView.as_view(), name='service-delete'),
    path('service/retrieve/', ServiceRenderedRetrieveAPIView.as_view(), name='service-retrieve'),
              ] + router_house.urls + router_flat.urls + router_water_meter.urls + router_tariff.urls
