from google.appengine.ext import ndb
from datetime import datetime

__all__ = ['Location',
           'Incident',
           'User']


class GBModel(ndb.Model):
    created_at = ndb.DateTimeProperty(required=True)
    last_updated_at = ndb.DateTimeProperty(required=True)

    def put(self, **kwargs):
        if not self.created_at:
            self.created_at = self.last_updated_at = datetime.now()
        else:
            self.last_updated_at = datetime.now()

        return super(GBModel, self).put(**kwargs)


class Location(GBModel):
    lat = ndb.FloatProperty(required=True)
    lng = ndb.FloatProperty(required=True)

    provider = ndb.StringProperty()
    accuracy = ndb.FloatProperty()
    altitude = ndb.FloatProperty()
    bearing = ndb.FloatProperty()
    speed = ndb.FloatProperty()


class Incident(GBModel):
    user_key = ndb.KeyProperty()
    location = ndb.StructuredProperty(Location,
                                      required=True)

    reported_by = ndb.StringProperty(required=True,
                                     choices=['AGENT', 'USER', 'AUTO'],
                                     default='AUTO')


class User(GBModel):
    username = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)

    location = ndb.StructuredProperty(Location,
                                      required=False)

    last_incident = ndb.KeyProperty(Incident,
                                    required=False)
