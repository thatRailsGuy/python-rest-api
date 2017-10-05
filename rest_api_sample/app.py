import falcon

from rest_api_sample.controllers.users import Resource

api = application = falcon.API()

users = Resource()
api.add_route('/users', users)