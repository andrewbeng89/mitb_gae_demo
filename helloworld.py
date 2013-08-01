import webapp2
from webapp2_extras import json


class API(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        hello_world = {
                'hello': 'world',
                'key': 'value',
                'another': 'test'
            }
        self.response.write(json.encode(hello_world))

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.redirect('/public/index.html')

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/api', API)
], debug=True)