# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from ..filters import ReviewFilter
from ..models import Pound, Review, Fish


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def home(request):
    reviews_list = Review.objects.all()
    fishes = Fish.objects.all()
    pounds = Pound.objects.all()

    filter = ReviewFilter(request.GET, queryset=reviews_list)
    reviews = filter.qs

    return render(request, 'app/home.html', {"reviews": reviews, "filter": filter, "fishes": fishes, "pounds": pounds})


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/sign_up.html'


def bootstrap_test(request):
    return render(request, 'app/bootstrap_test.html')