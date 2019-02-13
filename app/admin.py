# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Pound, Fish, Review

# Register your models here.


admin.site.register(Pound)
admin.site.register(Fish)
admin.site.register(Review)
