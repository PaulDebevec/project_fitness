# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0006_auto_20161022_1006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbmiprofile',
            name='weight',
        ),
        migrations.AddField(
            model_name='userbmiprofile',
            name='Weight',
            field=models.FloatField(default=150, help_text='Enter weight in pounds'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_weight',
            field=models.FloatField(default=150, help_text='Enter weight in pounds'),
        ),
    ]