# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.db import models
from django.utils.timezone import now


EASY = 'E'
MEDIUM = 'M'
HARD = 'H'
CATCH_EASE = ((EASY, 'легко'), (MEDIUM, 'средне'), (HARD, 'сложно'))
# CATCH_EASE = {EASY: 'легко', MEDIUM: 'средне', HARD: 'сложно'}


class Method(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Метод ловли'


class Fish(models.Model):
    name = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='fishes', default='fishes/no-img.jpg')
    catch_ease = models.CharField(max_length=1, default=MEDIUM, choices=CATCH_EASE)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Рыба'
        verbose_name_plural = 'Рыбы'


class Photo(models.Model):
    # pound = models.ForeignKey(Pound, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='pound_photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
class Pound(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    fishes = models.ManyToManyField(Fish)
    lang = models.FloatField(default=50)
    lat = models.FloatField(default=50)
    is_paid = models.BooleanField(default=False)
    contacts = models.CharField(blank=True, max_length=200)
    conditions = models.CharField(blank=True, max_length=400)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Пруд'
        verbose_name_plural = 'Пруды'





class Review(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # pound = models.ForeignKey(Pound, on_delete=models.CASCADE, blank=True, null=True, default=lambda: Pound.objects.all().first())
    pound = models.ForeignKey(Pound, on_delete=models.CASCADE, blank=True, null=True, default=1)
    content = models.TextField()
    # fish_caught = models.ForeignKey(Fish, on_delete=models.CASCADE, blank=True, null=True, default=lambda: Fish.objects.all().first())
    fish_caught = models.ForeignKey(Fish, on_delete=models.CASCADE, default=1)
    created_date = models.DateTimeField(
            default=timezone.now)
    # fishing_date = models.DateField(default=lambda: now().date())
    fishing_date = models.DateField(default=now().date())
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True)
    likes = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999)], blank=True, null=True)
    lang = models.FloatField(default=50)
    lat = models.FloatField(default=50)
    picture = models.ImageField(upload_to='reviews', default='reviews/no-img.jpg')
    length = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    method = models.ForeignKey(Method, on_delete=models.CASCADE, default=1)

    def __unicode__(self):
        return str(self.id)


    class Meta:
        verbose_name = 'Обзор'
        verbose_name_plural = 'Обзоры'
