from rest_framework import routers
from app.viewsets import FishViewSet

router = routers.DefaultRouter()

router.register(r'fish', FishViewSet)