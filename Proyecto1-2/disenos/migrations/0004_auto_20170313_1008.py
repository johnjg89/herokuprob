# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-13 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disenos', '0003_auto_20170313_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='estado',
            field=models.CharField(default='En proceso', max_length=100),
        ),
    ]