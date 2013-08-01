import webapp2
from webapp2_extras import json


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        hello_world = {
                'hello': 'world',
                'key': 'value',
                'another': 'test',
                'json': 'object'
            }
        self.response.write(json.encode(hello_world))


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)