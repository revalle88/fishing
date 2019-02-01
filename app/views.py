# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Pound, Review
from .forms import PoundForm, ReviewForm

from django.shortcuts import redirect


# Create your views here.
def home(request):
    reviews = Review.objects.all()
    return render(request, 'app/home.html', {"reviews": reviews})


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
    return render(request, 'app/review_show.html', {'review': review})
