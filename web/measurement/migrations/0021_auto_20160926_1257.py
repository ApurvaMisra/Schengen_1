# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-26 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0020_auto_20160920_1210'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Traceroute12',
            new_name='Traceroutemeasurement12',
        ),
        migrations.RenameField(
            model_name='relation12',
            old_name='traceroute12',
            new_name='traceroutemeasurement12',
        ),
        migrations.AlterField(
            model_name='traceroutemeasurement12',
            name='countries',
            field=models.ManyToManyField(through='measurement.Relation12', to='measurement.Countries'),
        ),
    ]
