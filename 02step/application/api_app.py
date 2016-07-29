# coding=utf-8
from application import app
from models import Location

__all__ = ['not_api']


@app.route('/api/Location', methods=['GET'])
def list_location():
    l = Location()
    l.lat = 1.0
    l.lng = 1.0
    l.put()

    vals = ''
    q = Location.query()

    n = q.count()

    for e in q:
        vals += str(e) + '<br><br>'
        # e.key.delete()

    return '<h3>%d</h3><br>%s' % (n, vals)
