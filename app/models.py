# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models


class Fish(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Create your models here.
class Pound(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    fishes = models.ManyToManyField(Fish)

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    pound = models.ForeignKey(Pound, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    fish_caught = models.ManyToManyField(Fish)
    created_date = models.DateTimeField(
            default=timezone.now)
    fishing_date = models.DateTimeField(
            default=timezone.now)
    rating = models.IntegerField()
    lang = models.FloatField(default=50)
    lat = models.FloatField(default=50)

