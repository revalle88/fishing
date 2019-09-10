# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from ..services.weather import WeatherManager
from ..models import Pound, Review, Photo
from ..forms import PoundForm

from django.shortcuts import redirect


def pound_list(request):
    pounds = Pound.objects.all()
    return render(request, 'app/pound_list.html', {"pounds": pounds})


def pound_show(request, id):
    pound = Pound.objects.filter(id=id)[0]
    point = {"lat": pound.lat, "lang": pound.lang}
    reviews = Review.objects.filter(pound=pound)
    weather = WeatherManager().get_weather(pound.lat, pound.lang)
    photos_list = Photo.objects.filter(pound_id=id)
    return render(
        request,
        'app/pound_details.html',
        {"pound": pound, "point": point, "reviews": reviews, "weather": weather, "photos": photos_list}
    )


def pound_new(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        form = PoundForm(request.POST)
        if form.is_valid():
            pound = form.save(commit=False)
            pound.author = request.user
            pound.save()
            return redirect('pounds')
    else:
        lat = request.GET.get('lat', 'lat none')
        lang = request.GET.get('lang', 'lang none')
        form = PoundForm(initial={'lat': lat, 'lang': lang})
        return render(request, 'app/pound_edit.html', {'form': form})


