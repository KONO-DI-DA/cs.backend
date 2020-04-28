from rest_framework import serializers
from main.models import Players, Room, Items, Season

class PlayersSerializer(serializers.ModelSerializer):
  class Meta:
    model = Players
    fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
  class Meta:
    model = Room
    fields = '__all__'

class ItemsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Items
    fields = '__all__'

class SeasonSerializer(serializers.ModelSerializer):
  class Meta:
    model = Season
    fields = '__all__'