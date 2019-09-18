# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from ..models import Fish


def fishes_list(request):
    fishes = Fish.objects.all()
    return render(request, 'app/fish_list.html', {"fishes": fishes})


def fish_details(request, slug):
    fish = Fish.objects.filter(slug=slug)[0]
    return render(request, 'app/fish_details.html', {"fish": fish})
