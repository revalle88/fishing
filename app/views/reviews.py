# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# import redis

from ..services.weather import WeatherManager
from django.forms import modelformset_factory
from django.shortcuts import render

from ..models import Review
from ..forms import ReviewForm

from django.shortcuts import redirect

import urllib.request
import json


def review_new(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('pounds')
    else:
        lat = request.GET.get('lat', 'lat none')
        lang = request.GET.get('lang', 'lang none')
        form = ReviewForm(initial={'lat': lat, 'lang': lang})
        return render(request, 'app/review_add.html', {'form': form})


def review_show(request, id):
    review = Review.objects.filter(id=id)[0]
    weather = WeatherManager().get_weather(review.lat, review.lang)
    point = {"lat": review.lat, "lang": review.lang}
    return render(
        request, 'app/review_show.html', {'review': review, 'weather': weather, "point": point}
    )
