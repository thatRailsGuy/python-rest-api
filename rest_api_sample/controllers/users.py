import json

import falcon


class Resource(object):

    # get /users
    def on_get(self, req, resp):
        doc = {
            'users': [
                {
                    'username': 'user1',
                    'email': 'user1@gmail.com'
                }
            ]
        }

        # Create a JSON representation of the resource
        resp.body = json.dumps(doc, ensure_ascii=False)

        # The following line can be omitted because 200 is the default
        # status returned by the framework, but it is included here to
        # illustrate how this may be overridden as needed.
        resp.status = falcon.HTTP_200