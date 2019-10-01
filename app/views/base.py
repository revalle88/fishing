# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from ..filters import ReviewFilter, MapFilter
from ..models import Pound, Review, Fish, Method

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def home(request):
    reviews_list = Review.objects.all()
    fishes = Fish.objects.all()
    pounds = Pound.objects.all()

    filter = ReviewFilter(request.GET, queryset=reviews_list)
    reviews = filter.qs
    has_filter = any(field in request.GET for field in set(filter.get_fields()))
    map_filter = MapFilter()
    filter_params = {}
    fish_caught = ''
    method_filter = ''
    entity_filter = ''
    if request.method == "POST":
        if request.POST.get('method') is not None:
            method_filter = ','.join(request.POST.getlist('method'))
        if request.POST.get('fish_caught') is not None:
            fish_caught = ','.join(request.POST.getlist('fish_caught'))
        if request.POST.get('entity_type') is not None:
            entity_filter = ','.join(request.POST.getlist('entity_type'))

    return render(
        request, 'app/home.html', {
            "reviews": reviews, "filter": filter, "fishes": fishes, "pounds": pounds,
            'has_filter': has_filter, 'map_filter': map_filter,
            'filter_params': filter_params, 'fish_filter': fish_caught,
            'method_filter': method_filter, 'entity_filter': entity_filter
        }
    )


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/sign_up.html'


def bootstrap_test(request):
    return render(request, 'app/bootstrap_test.html')