# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0016_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electronicsales',
            name='payment',
            field=models.FloatField(default=0.0),
        ),
    ]
