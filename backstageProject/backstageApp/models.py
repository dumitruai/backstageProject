from django.db import models


class SensorData(models.Model):
    serial = models.CharField(max_length=12)
    application = models.IntegerField()
    timestamp = models.DateTimeField()
    sensor_type = models.CharField(max_length=4)
    device = models.CharField(max_length=20)
    v0 = models.IntegerField()
    dwell_time = models.FloatField()


