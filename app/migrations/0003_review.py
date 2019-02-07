# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-24 06:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20190117_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('rating', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('fish_caught', models.ManyToManyField(to='app.Fish')),
                ('pound', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Pound')),
            ],
        ),
    ]