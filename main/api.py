from main.models import Main
from rest_framework import viewsets, permissions
from .serializers import MainSerializer

# Main Viewset
class MainViewSet(viewsets.ModelViewSet):
  queryset = Main.objects.all()
  permission_classes = [
    permissions.AllowAny
  ]
  serializer_class = MainSerializer