# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from ..models import Article, Category


def article_list(request):
    categories = Category.objects.all()
    articles = Article.objects.all()
    return render(
        request, 'app/article_list.html',
        {"articles": articles, "categories": categories}
    )


def blog_category_list(request, slug):
    categories = Category.objects.all()
    current_category = Category.objects.filter(slug=slug)[0]
    articles = Article.objects.filter(category=current_category)
    return render(
        request, 'app/article_list.html',
        {"articles": articles, "categories": categories}
    )


def article_show(request, id):
    article = Article.objects.filter(id=id)[0]
    return render(request, 'app/article_show.html', {"article": article})
