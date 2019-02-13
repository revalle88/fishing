# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Pound, Review, Fish
from .forms import PoundForm, ReviewForm

from django.shortcuts import redirect

import urllib
import json


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.
def home(request):
    reviews = Review.objects.all()
    fishes = Fish.objects.all()
    return render(request, 'app/home.html', {"reviews": reviews, "fishes": fishes})


def pound_list(request):
    pounds = Pound.objects.all()
    return render(request, 'app/pound_list.html', {"pounds": pounds})


def pound_new(request):
    if request.method == "POST":
        form = PoundForm(request.POST)
        if form.is_valid():
            pound = form.save(commit=False)
            pound.author = request.user
            pound.save()
            return redirect('pounds')
    else:
        form = PoundForm()
        return render(request, 'app/pound_edit.html', {'form': form})


def review_new(request):
    if request.method == "POST":
        print("!!!!POST")
        form = ReviewForm(request.POST)
        print("Get FOrm")
        if form.is_valid():
            print("Valid")
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('pounds')
    else:
        lat = request.GET.get('lat', 'lat none')
        lang = request.GET.get('lang', 'lang none')
        form = ReviewForm(initial={'lat': lat, 'lang': lang})

        print(request.GET.get('lang', 'lang none'))
        print(request.GET.get('lat', 'lat none'))
        return render(request, 'app/review_add.html', {'form': form})


def review_show(request, id):
    print(id)
    review = Review.objects.filter(id=id)[0]
    r_id = request.GET.get('lat', 'lat none')
    resp = urllib.urlopen("https://api.darksky.net/forecast/caf0208379875df865f2185f5246bf48/53.8267,45.4233?units = auto").read()
    resp_jsonified = json.loads(resp)
    print(resp_jsonified.get('currently')['temperature'])
    weather = resp_jsonified.get('currently')
    return render(request, 'app/review_show.html', {'review': review, 'weather': weather})


def fishes_list(request):
    fishes = Fish.objects.all()
    return render(request, 'app/fish_list.html', {"fishes": fishes})


def fish_details(request, id):
    fish = Fish.objects.filter(id=id)[0]
    return render(request, 'app/fish_details.html', {"fish": fish})


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/sign_up.html'