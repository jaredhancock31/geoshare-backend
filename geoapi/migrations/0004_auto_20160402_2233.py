# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-02 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoapi', '0003_auto_20160402_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='droplet',
            name='timestamp',
            field=models.TextField(max_length=200),
        ),
    ]