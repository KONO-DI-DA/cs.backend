from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Players(models.Model):
  name = models.CharField(max_length=25)
  room_id = models.IntegerField()
  item_id = models.IntegerField()
  owner = models.ForeignKey(User, related_name='main', on_delete=models.CASCADE, null=True)

class Room(models.Model):
  name = models.CharField(max_length=50)
  season_id = models.IntegerField()
  left_id = models.IntegerField()
  right_id = models.IntegerField()
  up_id = models.IntegerField()
  down_id = models.IntegerField()
  outside_id = models.IntegerField()
  inside_id = models.IntegerField()
  item_id = models.IntegerField()
  top_tile = models.IntegerField()
  bottom_tile = models.IntegerField()

class Items(models.Model):
  season_id = models.IntegerField()
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=50)

class Season(models.Model):
  name = models.CharField(max_length=50)
  is_solved = models.IntegerField()