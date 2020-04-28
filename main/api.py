from main.models import Players, Room, Items, Season
from rest_framework import viewsets, permissions
from .serializers import PlayersSerializer, RoomSerializer, ItemsSerializer, SeasonSerializer

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

class RoomViewSet(viewsets.ModelViewSet):
  queryset = Room.objects.all()
  permission_classes = [
    permissions.IsAuthenticated
  ]
  serializer_class = RoomSerializer
  
  def perform_create(self, serializer):
    serializer.save()

class ItemsViewSet(viewsets.ModelViewSet):
  queryset = Items.objects.all()
  permission_classes = [
    permissions.IsAuthenticated
  ]
  
  serializer_class = ItemsSerializer

  def perform_create(self, serializer):
    serializer.save()

class SeasonViewSet(viewsets.ModelViewSet):
  queryset=Season.objects.all()
  permission_classes = [
    permissions.IsAuthenticated
  ]
  
  serializer_class = SeasonSerializer

  def perform_create(self, serializer):
    serializer.save()
