from main.models import Players
from rest_framework import viewsets, permissions
from .serializers import PlayersSerializer

# Player Viewset
class PlayersViewSet(viewsets.ModelViewSet):
  permission_classes = [
    permissions.IsAuthenticated
  ]
  
  serializer_class = PlayersSerializer

  def get_queryset(self):
    return self.request.user.main.all()

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)
