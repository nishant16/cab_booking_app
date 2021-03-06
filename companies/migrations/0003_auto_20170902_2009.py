# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-02 20:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_cab_driver_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('mobile_no', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='cab',
            old_name='driver_name',
            new_name='helpline_no',
        ),
        migrations.RemoveField(
            model_name='cab',
            name='cab_name',
        ),
        migrations.AddField(
            model_name='cab',
            name='name',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='cab',
            name='refer_and_earn',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cab',
            name='support',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='cab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Cab'),
        ),
    ]
