from rest_framework import viewsets, status
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

# Добавление метода create в MeasurementViewSet
class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def create(self, request, *args, **kwargs):
        sensor_id = request.data.get('sensor')
        try:
            sensor = Sensor.objects.get(pk=sensor_id)
        except Sensor.DoesNotExist:
            return Response({'detail': 'Sensor not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(sensor=sensor)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# Добавление метода perform_destroy в SensorViewSet
class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def perform_destroy(self, instance):
        instance.measurements.all().delete()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
