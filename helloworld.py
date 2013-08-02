import webapp2
from webapp2_extras import json

class APIRootHandler(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        hello_world = {
                'hello': 'world',
                'key': 'value',
                'another': 'test'
            }
        self.response.write(json.encode(hello_world))

application = webapp2.WSGIApplication([
    ('/api/', APIRootHandler)
], debug=True)