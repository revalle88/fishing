from django.http import JsonResponse
from django.views import View
from django.http import QueryDict

from ..forms import PhotoForm
from ..models import Photo


class BasicUploadView(View):
    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)

    def delete(self, request):
        params = QueryDict(self.request.body)
        photo_id = params.get('photo_id')
        print(photo_id)
        Photo.objects.filter(id=photo_id).delete()
        data = {'success': True}
        return JsonResponse(data)
