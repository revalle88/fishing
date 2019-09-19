from django.contrib.staticfiles.templatetags.staticfiles import static
from django.http import JsonResponse
from django.urls import reverse
from django.views import View

from app.models import Review, Pound


class MapRenderView(View):
    def post(self, request):
        reviews = Review.objects.all()
        pounds = Pound.objects.all()
        print('here AJAX!!!')
        # print(reverse('fish_details', 'carp'))
        features = []
        geo_id = 0
        #add reviews
        for review in reviews:
            item = {
                "type": "Feature",
                "id": geo_id,
                "geometry": {
                    "type": "Point",
                    "coordinates": [review.lat, review.lang]
                },
                "properties": {
                    "balloonContent": str(review.fishing_date)+"<br>Поймано: <a href = 'fishes/"+review.fish_caught.slug+"'>"+review.fish_caught.name+"</a><br><a href = 'reviews/"+str(review.id)+"'>Детали...</a>",
                    "clusterCaption": "Еще одна метка",
                    "hintContent": "Текст подсказки"
                }
            }
            features.append(item)
            geo_id = geo_id + 1
        # add pounds
        for pound in pounds:
            print(geo_id)
            item = {
                "type": "Feature",
                "id": geo_id,
                "geometry": {
                    "type": "Point",
                    "coordinates": [pound.lat, pound.lang]
                },
                "properties": {
                    "balloonContent": "<a href = 'pounds/"+pound.slug+"'>"+pound.name+"</a>",
                    "clusterCaption": "Еще одна метка",
                    "hintContent": "Текст подсказки",
                }
                # "options": {
                #     "iconLayout": 'default#image',
                #     "iconImageHref": static('catch_icon.png'),
                #     "iconImageSize": [24, 24],
                #     "iconImageOffset": [-10, -5],
                # }
            }
            features.append(item)
            geo_id = geo_id + 1
        data = {"type": "FeatureCollection", "features": features}
        return JsonResponse(data)


# balloonContent: "{{review.fishing_date}}<br>Поймано: <a href = {% url 'fish_details' review.fish_caught.id %}>{{review.fish_caught.name}}</a><br><a href = {% url 'review_show' review.id %}>Детали...</a>"