# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from ..models import Pound, Review
from ..forms import PoundForm

from django.shortcuts import redirect


def pound_list(request):
    pounds = Pound.objects.all()
    return render(request, 'app/pound_list.html', {"pounds": pounds})


def pound_show(request, id):
    pound = Pound.objects.filter(id=id)[0]
    point = {"lat": pound.lat, "lang": pound.lang}
    reviews = Review.objects.filter(pound=pound)
    return render(request, 'app/pound_details.html', {"pound": pound, "point": point, "reviews": reviews})


def pound_new(request):
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