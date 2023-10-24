from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CheckProfileView, ProfileViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('check-profile/', CheckProfileView.as_view(), name='check-profile'),
    path('', include(router.urls)),
]