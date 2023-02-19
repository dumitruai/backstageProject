import base64
import json

import pydash as pydash
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

from backstageProject.backstageApp.models import SensorData
from backstageProject.backstageApp.serializers import SensorDataSerializer


@api_view(['POST'])
@csrf_exempt
def pubsub_handler(request):
    r_status = status.HTTP_400_BAD_REQUEST
    r_data = dict(message="No data provided")
    try:
        sensor_data = pydash.get(request.data, 'message.data', None)
        sensor_data = base64.b64decode(sensor_data)
        sensor_data = json.loads(sensor_data)
        SensorData.objects.create(
            serial=sensor_data['serial'],
            application=sensor_data['application'],
            timestamp=sensor_data['Time'],
            sensor_type=sensor_data['Type'],
            device=sensor_data['device'],
            v0=sensor_data['v0'],
            dwell_time=sensor_data['v18']
        )
        r_data = dict(message="Succesfuly registered a new record")
        r_status = status.HTTP_200_OK
    except Exception as ex:
        r_data = dict(message=str(ex))
    return Response(
        status=r_status,
        data=r_data
    )

@api_view(['GET'])
@csrf_exempt
def get_sensor_data(request):
    return Response(
        status=status.HTTP_200_OK,
        data=SensorDataSerializer(SensorData.objects.all(),many=True).data
    )

@api_view(['GET'])
@csrf_exempt
def get_chart_data(request):
    r_status = status.HTTP_200_OK
    r_data = []
    sensor_data = SensorData.objects.all()
    try:
        for data in sensor_data:
            r_data.append(
                dict(
                    serial=data.serial,
                    timestamp=data.timestamp,
                    dwell_time=data.dwell_time
                )
            )
        return Response(
            status=r_status,
            data=r_data
        )
    except Exception as ex:
        r_data = dict(message=str(ex))
    return Response(
        status=r_status,
        data=r_data
    )
