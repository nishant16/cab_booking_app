# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-02 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cab',
            name='driver_name',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
