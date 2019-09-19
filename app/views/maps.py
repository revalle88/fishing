from django.http import JsonResponse
from django.urls import reverse
from django.views import View

from ..models import Review


class MapRenderView(View):
    def post(self, request):
        reviews = Review.objects.all()
        print('here AJAX!!!')
        # print(reverse('fish_details', 'carp'))
        features = []
        for review in reviews:
            print("this!")
            print(review.lat)
            item = {
                "type": "Feature",
                "id": review.id,
                "geometry": {
                    "type": "Point",
                    "coordinates": [review.lat, review.lang]},
                    "properties": {
                        "balloonContent": str(review.fishing_date)+"<br>Поймано: <a href = 'fishes/"+review.fish_caught.slug+"'>"+review.fish_caught.name+"</a><br><a href = 'reviews/"+str(review.id)+"'>Детали...</a>",
                        "clusterCaption": "Еще одна метка",
                        "hintContent": "Текст подсказки"
                    }
                   }
            features.append(item)
        data = {"type": "FeatureCollection", "features": features}
        return JsonResponse(data)


# balloonContent: "{{review.fishing_date}}<br>Поймано: <a href = {% url 'fish_details' review.fish_caught.id %}>{{review.fish_caught.name}}</a><br><a href = {% url 'review_show' review.id %}>Детали...</a>"