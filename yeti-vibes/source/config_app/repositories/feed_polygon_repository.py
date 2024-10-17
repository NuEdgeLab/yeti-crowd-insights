# config_app/repositories/FeedPolygonModel_repository.py
from config_app.models import Event, Feed, FeedPolygon as FeedPolygonModel
from config_app.domain_models.feed_polygon import FeedPolygon
from rest_framework.exceptions import NotFound


class FeedPolygonRepository:

    def create_feed_polygon(self, feed_id, event_id, data):
        try:
            event = Event.objects.get(event_id=event_id)
        except Event.DoesNotExist:
            raise NotFound("No Event Found")

        feed = Feed.objects.get(feed_id=feed_id, event=event)

        feed_polygon = FeedPolygonModel(**data)
        feed_polygon.save()
        feed_polygon.feeds.add(feed)

        return feed_polygon

    def get_all_feed_polygons(self, feed_id, event_id):
        try:
            event = Event.objects.get(event_id=event_id)
        except Event.DoesNotExist:
            raise NotFound("No Event Found")
        feed = Feed.objects.get(feed_id=feed_id, event=event)

        feed_polygons = FeedPolygonModel.objects.filter(feeds=feed)

        # return [
        #     FeedPolygon(polygon_id=feed_polygon.polygon_id, feed_id=feed_polygon.feed_id, polygon_name=feed_polygon.polygon_name, feed_polygons=feed_polygon.feed_polygons, polygon_color=feed_polygon.polygon_color) for feed_polygon in feed_polygons]
        return feed_polygons

    def get_feed_polygon(self, polygon_id, feed_id, event_id):
        try:
            event = Event.objects.get(event_id=event_id)
        except Event.DoesNotExist:
            raise NotFound("No Event Found")
        feed = Feed.objects.get(feed_id=feed_id, event=event)
        try:
            feed_polygon = FeedPolygonModel.objects.get(
                feed=feed, polygon_id=polygon_id)
        except FeedPolygonModel.DoesNotExist:
            raise NotFound("FeedPolygon matching query does not exist.")
        return FeedPolygon(polygon_id=feed_polygon.polygon_id, feed_id=feed_polygon.feed, polygon_name=feed_polygon.polygon_name, feed_polygons=feed_polygon.feed_polygons, polygon_color=feed_polygon.polygon_color)

    def update_feed_polygon(self, polygon_id, feed_id, event_id, data):
        try:
            event = Event.objects.get(event_id=event_id)
        except Event.DoesNotExist:
            raise NotFound("No Event Found")
        feed = Feed.objects.get(id=feed_id, event=event)
        try:
            feed_polygon = FeedPolygonModel.objects.get(
                feed=feed, polygon_id=polygon_id)
        except FeedPolygonModel.DoesNotExist:
            raise NotFound("FeedPolygon matching query does not exist.")

        for key, value in data.items():
            setattr(feed_polygon, key, value)
        feed_polygon.save()
        return FeedPolygon(polygon_id=feed_polygon.polygon_id, feed_id=feed_polygon.feed_id, polygon_name=feed_polygon.polygon_name, feed_polygons=feed_polygon.feed_polygons, polygon_color=feed_polygon.polygon_color)

    def delete_feed_polygon(self, polygon_id, feed_id, event_id):
        try:
            event = Event.objects.get(event_id=event_id)
        except Event.DoesNotExist:
            raise NotFound("No Event Found")

        feed = Feed.objects.get(id=feed_id, event=event)
        try:
            feed_polygon = FeedPolygonModel.objects.get(
                feed=feed, polygon_id=polygon_id)
        except FeedPolygonModel.DoesNotExist:
            raise NotFound("FeedPolygon matching query does not exist.")

        feed_polygon.delete()
        return {"success": True}
