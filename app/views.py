# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
def pound_list(request):
    return render(request, 'app/pound_list.html', {})
