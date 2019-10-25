from django.contrib.staticfiles.templatetags.staticfiles import static
from django.http import JsonResponse
from django.urls import reverse
from django.views import View

from app.filters import ReviewFilter
from app.models import Review, Pound


class MapRenderView(View):
    def post(self, request):
        reviews = Review.objects.all()
        entity_filter_types = []
        if len(request.POST.get('fish_filter'))>0:
            fish_filter_ids = request.POST.get('fish_filter').split(',')
            reviews = reviews.filter(fish_caught__in=fish_filter_ids)

        if len(request.POST.get('method_filter'))>0:
            method_filter_ids = request.POST.get('method_filter').split(',')
            reviews = reviews.filter(method__in=method_filter_ids)

        if len(request.POST.get('entity_filter'))>0:
            entity_filter_types = request.POST.get('entity_filter').split(',')
            print(entity_filter_types)

        pounds = Pound.objects.all()
        print('here AJAX!!!')
        print(request.POST)
        # print(reverse('fish_details', 'carp'))
        features = []
        geo_id = 0
        #add reviews
        if '1' in entity_filter_types or len(entity_filter_types) == 0:
            # add reviews
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
                    },
                    "options": {
                        "iconLayout": 'default#image',
                        "iconImageHref": static('images/icons/catch_icon.png'),
                        "iconImageSize": [24, 24],
                        "iconImageOffset": [-10, -5],
                    }
                }
                features.append(item)
                geo_id = geo_id + 1
        # add pounds
        if '2' in entity_filter_types or len(entity_filter_types) == 0:
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
                    },
                    "options": {
                        "iconLayout": 'default#image',
                        "iconImageHref": static('images/icons/pound_icon.png'),
                        "iconImageSize": [24, 24],
                        "iconImageOffset": [-10, -5],
                    }
                }
                features.append(item)
                geo_id = geo_id + 1
        data = {"type": "FeatureCollection", "features": features}
        return JsonResponse(data)
