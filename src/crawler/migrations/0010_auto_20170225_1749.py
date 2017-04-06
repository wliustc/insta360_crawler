# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-25 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0009_abroadsales_googleindex_sharechannel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareMode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_group_id', models.CharField(blank=True, max_length=200)),
                ('mode', models.CharField(blank=True, max_length=200)),
                ('date', models.DateField()),
                ('version', models.CharField(blank=True, max_length=200)),
                ('count', models.IntegerField(default=0)),
                ('device', models.IntegerField(default=0)),
                ('count_per_launch', models.FloatField(default=0.0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]