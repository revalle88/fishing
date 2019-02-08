# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-07 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190207_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='fish',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fish',
            name='picture',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/'),
        ),
    ]
