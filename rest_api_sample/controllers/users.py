import json
import falcon

from rest_api_sample.models.user import User

FIELDS = {
    'username': {
        'type': 'string',
        'required': True,
        'minlength': 4,
        'maxlength': 20
    },
    'email': {
        'type': 'string',
        'required': True,
        'maxlength': 320
    },
    'password': {
        'type': 'string',
        'required': True,
        'minlength': 8,
        'maxlength': 64
    },
    'phone': {
        'type': 'string',
        'required': False
    },
    'address': {
        'type': 'string',
        'required': False
    },
    'additional_info': {
        'type': 'string',
        'required': False
    },
    'is_admin': {
        'type': 'boolean',
        'required': True
    }
}


class Resource(object):

    # get /users
    def on_get(self, req, resp):
        resp.body = json.dumps(User.find_all(), ensure_ascii=False)

        # The following line can be omitted because 200 is the default
        # status returned by the framework, but it is included here to
        # illustrate how this may be overridden as needed.
        resp.status = falcon.HTTP_200