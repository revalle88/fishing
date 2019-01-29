from rest_framework import viewsets
from .models import Fish
from .serializers import FishSerializer


class FishViewSet(viewsets.ModelViewSet):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer
