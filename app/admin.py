# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Pound, Fish, Review

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


admin.site.register(Pound)
admin.site.register(Review)


class FishAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = 'description'


admin.site.register(Fish, FishAdmin)