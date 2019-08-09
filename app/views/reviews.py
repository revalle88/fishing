# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import modelformset_factory
from django.shortcuts import render

from ..models import Review, Images
from ..forms import ReviewForm, ImageForm

from django.shortcuts import redirect

import urllib.request
import json


def review_new(request):
    if not request.user.is_authenticated:
        return redirect('login')

    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, extra=3)

    if request.method == "POST":
        print("!!!!POST")
        form = ReviewForm(request.POST)

        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())

        if form.is_valid() and formset.is_valid():
            print("Valid")
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            form.save_m2m()
            for image_form in formset.cleaned_data:
                if image_form:
                    image = image_form['image']
                    photo = Images(review=review, image=image)
                    photo.save()
            return redirect('pounds')
    else:
        lat = request.GET.get('lat', 'lat none')
        lang = request.GET.get('lang', 'lang none')
        form = ReviewForm(initial={'lat': lat, 'lang': lang})
        formset = ImageFormSet(queryset=Images.objects.none())
        return render(request, 'app/review_add.html', {'form': form, 'formset': formset})


def review_show(request, id):
    print(id)
    review = Review.objects.filter(id=id)[0]
    with urllib.request.urlopen("https://api.darksky.net/forecast/caf0208379875df865f2185f5246bf48/53.8267,45.4233?units=auto") as url:
        resp = url.read()
    print(resp)
    resp_jsonified = json.loads(resp)
    print(resp_jsonified.get('currently')['temperature'])
    weather = resp_jsonified.get('currently')
    point = {"lat": review.lat, "lang": review.lang}
    fish_caught = review.fish_caught.all()
    print(fish_caught)
    return render(
        request, 'app/review_show.html', {'review': review, 'weather': weather, "point": point, 'fish_caught': fish_caught}
    )
