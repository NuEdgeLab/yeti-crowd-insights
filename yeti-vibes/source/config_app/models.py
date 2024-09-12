from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.client_name


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="client")
    event_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=False)
    is_active = models.BooleanField(default= True)
    
    def __str__(self):
        return self.event_name
    
    
class Feed(models.Model):
    feed_id = models.AutoField(primary_key=True)
    feed_event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event")
    feed_name = models.CharField(max_length=200)
    rtsp_link = models.URLField(max_length=200)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.feed_name


class FeedPolygon(models.Model):
    polygon_id = models.AutoField(primary_key=True)
    feed_id = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name="feed")
    polygon_name = models.CharField(max_length=255)

    # Storing polygon as a list of tuples
    polygon = ArrayField(
        ArrayField(models.IntegerField(), size=2),
        size=5
    )

    # Storing color as an array of integers
    polygon_color = ArrayField(models.IntegerField(), size=3)

    def __str__(self):
        return self.polygon_name
