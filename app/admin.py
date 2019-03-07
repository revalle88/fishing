# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Pound, Fish, Review, Tag, Article, Category

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


admin.site.register(Pound)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Category)


class ArticleAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = 'content'

class FishAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = 'description'


admin.site.register(Article, ArticleAdmin)
admin.site.register(Fish, FishAdmin)