# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-28 09:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0003_mediafans'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MediaFans',
            new_name='MediaFan',
        ),
    ]