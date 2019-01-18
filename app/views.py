# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Pound
from .forms import PoundForm

from django.shortcuts import redirect


# Create your views here.
def home(request):
    return render(request, 'app/home.html', {})


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