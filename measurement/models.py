from django.db import models
from django.db.models.fields.files import ImageField


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = ImageField(null=True, blank=True, upload_to='measurement_images/')

    def __str__(self):
        return f"Measurement for {self.sensor.name} at {self.created_at}"