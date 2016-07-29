# coding=utf-8
from application import app

__all__ = ['not_api']


@app.route('/api', methods=['GET'])
def not_api():

    return 'It\'s not an API'
