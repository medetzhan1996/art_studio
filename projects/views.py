from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Project, Visualization, Plan, Detail
from .serializers import (ProjectSerializer, VisualizationSerializer,
                          PlanSerializer, DetailSerializer)


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class VisualizationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Visualization.objects.all()
    serializer_class = VisualizationSerializer


class PlanViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class DetailViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer

    @action(detail=True, methods=['POST'], url_path='publish')
    def publish_project(self, request, pk=None):
        project = self.get_object()
        project.is_draft = False
        project.save()
        return Response({"status": "Project published successfully"})
