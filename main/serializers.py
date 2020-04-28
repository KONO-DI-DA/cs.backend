from rest_framework import serializers
from main.models import Players, Room, Items, Season

class PlayersSerializer(serializers.ModelSerializer):
  class Meta:
    model = Players
    fields = '__all__'