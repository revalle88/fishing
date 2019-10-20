from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import View
from django.http import QueryDict

from ..forms import PhotoForm
from ..models import Photo, Pound


class BasicUploadView(View):
    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        print(1)
        print(self.request.POST)
        print(self.request.FILES)
        print(form.errors)
        if form.is_valid():
            print(2)
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url, 'id': photo.id}
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


def pound_images_clear(request, slug):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        print(request.POST['pound_id'])
        pound_id = request.POST['pound_id']
        Photo.objects.filter(pound_id=pound_id).delete()
        return redirect('pound_show', slug=slug)
