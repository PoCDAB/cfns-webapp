# Generated by Django 3.2 on 2021-07-05 21:08

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_aisdecoded_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geonotification',
            name='leftdowncorner',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='Pivot'),
        ),
        migrations.AlterField(
            model_name='geonotification',
            name='leftupcorner',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='Pivot'),
        ),
        migrations.AlterField(
            model_name='geonotification',
            name='rightdowncorner',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='Pivot'),
        ),
        migrations.AlterField(
            model_name='geonotification',
            name='rightuppercorner',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='Pivot'),
        ),
    ]
