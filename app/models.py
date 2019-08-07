# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.db import models


class Fish(models.Model):
    name = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='fishes', default='fishes/no-img.jpg')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Рыба'
        verbose_name_plural = 'Рыбы'


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
    pound = models.ForeignKey(Pound, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    fish_caught = models.ManyToManyField(Fish)
    created_date = models.DateTimeField(
            default=timezone.now)
    fishing_date = models.DateTimeField(
            default=timezone.now)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    lang = models.FloatField(default=50)
    lat = models.FloatField(default=50)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Обзор'
        verbose_name_plural = 'Обзоры'


class Photo(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    file = models.ImageField(upload_to="tmp_pics")
    description = models.TextField(blank=True, null=True)


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        default=timezone.now)
    published = models.BooleanField(default=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, default='')
    content = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='blog')
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __unicode__(self):
        return str(self.name)


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


def get_image_filename(instance, filename):
    slug = instance.review.id
    return "review_images/%s-%s" % (slug, filename)


class Images(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')










