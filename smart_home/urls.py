from django.urls import path

from measurement.views import SensorViewSet, MeasurementViewSet

urlpatterns = [
    path('sensors/', SensorViewSet.as_view({'get': 'list', 'post': 'create'}), name='sensors'),
    path('sensors/<int:pk>/', SensorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='sensor'),
    path('measurements/', MeasurementViewSet.as_view({'get': 'list', 'post': 'create'}), name='measurements'),
    path('measurements/<int:pk>/', MeasurementViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='measurement'),
]