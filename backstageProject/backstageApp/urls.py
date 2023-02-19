from django.urls import path

from backstageProject.backstageApp.views import pubsub_handler, get_sensor_data, get_chart_data

urlpatterns = [
    path('rest/pubsub-handler/', pubsub_handler, name='pubsub_handler'),
    path('rest/sensor-data/', get_sensor_data, name='get_sensor_data'),
    path('rest/sensor-graph/', get_chart_data, name='get_chart_data'),
]