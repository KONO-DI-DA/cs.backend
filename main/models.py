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
  season_id = models.IntegerField(default=0)
  left_id = models.IntegerField(default=0)
  right_id = models.IntegerField(default=0)
  up_id = models.IntegerField(default=0)
  down_id = models.IntegerField(default=0)
  outside_id = models.IntegerField(default=0)
  inside_id = models.IntegerField(default=0)
  item_id = models.IntegerField(default=0)
  top_tile = models.IntegerField(default=0)
  bottom_tile = models.IntegerField(default=0)

  def connectRooms(self, destinationRoom, direction):
    destinationRoomID = destinationRoom.id
    try:
      destinationRoom = Room.objects.get(id=destinationRoomID)
    except Room.DoesNotExist:
      print("That room does not exist")
    else:
      if direction == "up":
        self.up_id = destinationRoomID
      elif direction == "down":
        self.down_id = destinationRoomID
      elif direction == "left":
        self.left_id = destinationRoomID
      elif direction == "right":
        self.right_id = destinationRoomID
      elif direction == "inside":
        self.inside_id = destinationRoomID
      elif direction == "outside":
        self.outside_id = destinationRoomID
      else:
        print("Invalid direction")
        return
      self.save()
  
class Items(models.Model):
  season_id = models.IntegerField()
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=200)

class Season(models.Model):
  name = models.CharField(max_length=50)
  is_solved = models.IntegerField()