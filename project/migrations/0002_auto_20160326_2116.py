# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-26 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(blank=True, verbose_name='Deadline date'),
        ),
    ]