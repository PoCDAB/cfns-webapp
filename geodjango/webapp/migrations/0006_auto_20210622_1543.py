# Generated by Django 3.2 on 2021-06-22 15:43

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20210622_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aisdecoded',
            name='MMSI',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='aisdecoded',
            name='course',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='aisdecoded',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='aisdecoded',
            name='name',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
