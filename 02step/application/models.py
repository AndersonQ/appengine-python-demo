from google.appengine.ext import ndb

__all__ = ['Location']


class Location(ndb.Model):
    lat = ndb.FloatProperty(required=True)
    lng = ndb.FloatProperty(required=True)

    provider = ndb.StringProperty()
    accuracy = ndb.FloatProperty()
    altitude = ndb.FloatProperty()
    bearing = ndb.FloatProperty()
    speed = ndb.FloatProperty()
