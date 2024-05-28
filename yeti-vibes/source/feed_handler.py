import json
feed_path = '../json/feed_config.json'
polygon_path = '../json/feed_polygon.json'

# Use-Case: 160 - Load Feed Configuration
class FeedPolygon:
    def __init__(self):
        pass
    
    
# Use-Case: 160 - Load Feed Configuration
class FeedHandler:
    def __init__(self):
        self.feed = []

    # logic to load feeds and their polygons
    def load_feeds(self, feed_path, event_id):
        
        with open(feed_path, 'r') as f:
            data = json.load(f)
        
        for feed in data["feed_config"]:
            if (feed["EventId"] == event_id):   
                feed_id = feed["FeedId"]
                polygon = FeedPolygon()
                feed_polygons = polygon.load_polygons(feed_id=feed_id, polygon_path=polygon_path)
                feed['Polygons'] = feed_polygons
                self.feed.append(feed)
            return self.feed
        
        
# Use-Case: 160 - Load Feed Configuration
class Feed:
    def __init__(self):
        self.feed_polygons = []

    def load_polygons(self, feed_id, polygon_path):
        # logic to load the data on the basis of feed_id

        with open(polygon_path, 'r') as f:
            data = json.load(f)

        for polygon in data["feed_polygon"]:
            if (polygon['FeedId'] == feed_id):
                self.feed_polygons.append(polygon)

        return self.feed_polygons
