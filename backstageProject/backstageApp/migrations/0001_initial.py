# Generated by Django 4.1.7 on 2023-02-18 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=12)),
                ('application', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
                ('type', models.CharField(max_length=4)),
                ('device', models.CharField(max_length=20)),
                ('v0', models.IntegerField()),
                ('dwell_time', models.FloatField()),
            ],
        ),
    ]