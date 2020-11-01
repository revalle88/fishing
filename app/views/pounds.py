# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from ..services.weather import WeatherManager
from ..models import Pound, Review, Photo
from ..forms import PoundForm

from django.shortcuts import redirect
from django.views.generic import ListView


class PoundListView(ListView):
    model = Pound
    template_name = 'app/pound_list.html'

    def get_context_data(self, **kwargs):
        context = super(PoundListView, self).get_context_data(**kwargs)
        pounds = self.get_queryset()
        context['pounds'] = pounds
        return context

def pound_show(request, slug):
    pound = Pound.objects.filter(slug=slug)[0]
    point = {"lat": pound.lat, "lang": pound.lang}
    reviews = Review.objects.filter(pound=pound)
    weather = WeatherManager().get_weather(pound.lat, pound.lang)
    photos_list = Photo.objects.filter(pound_id=pound.id)
    fishes = pound.fishes.all()
    return render(
        request,
        'app/pound_details.html',
        {"pound": pound, "point": point, "reviews": reviews, "weather": weather, "photos": photos_list, "fishes": fishes}
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
            form.save_m2m()
            return redirect('pounds')
    else:
        lat = request.GET.get('lat', 'lat none')
        lang = request.GET.get('lang', 'lang none')
        form = PoundForm(initial={'lat': lat, 'lang': lang})
        return render(request, 'app/pound_edit.html', {'form': form})


