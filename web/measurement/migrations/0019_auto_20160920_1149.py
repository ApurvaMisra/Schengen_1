# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-20 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0018_auto_20160920_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relation12',
            name='quantity',
        ),
        migrations.AddField(
            model_name='traceroute12',
            name='countries',
            field=models.ManyToManyField(through='measurement.relation12', to='measurement.Countries'),
        ),
    ]
