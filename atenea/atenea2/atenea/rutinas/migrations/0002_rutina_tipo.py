# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-15 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rutinas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rutina',
            name='tipo',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]