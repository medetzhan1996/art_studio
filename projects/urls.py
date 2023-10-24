from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, VisualizationViewSet, PlanViewSet, DetailViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'visualizations', VisualizationViewSet)
router.register(r'plans', PlanViewSet)
router.register(r'details', DetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]