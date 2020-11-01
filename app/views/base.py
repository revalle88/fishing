# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from ..filters import MapFilter

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def home(request):
    map_filter = MapFilter()

    return render(
        request, 'app/home.html', {
            'map_filter': map_filter,
        }
    )


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/sign_up.html'


def bootstrap_test(request):
    return render(request, 'app/bootstrap_test.html')