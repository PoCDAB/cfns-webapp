# Generated by Django 3.2 on 2021-06-22 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20210622_1251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ais',
            options={'verbose_name': 'Encoded AIS message', 'verbose_name_plural': 'Encoded AIS messages'},
        ),
        migrations.AlterModelOptions(
            name='aisdecoded',
            options={'verbose_name': 'Decoded AIS message', 'verbose_name_plural': 'Decoded AIS messages'},
        ),
        migrations.AlterField(
            model_name='aisdecoded',
            name='MMSI',
            field=models.IntegerField(),
        ),
    ]
