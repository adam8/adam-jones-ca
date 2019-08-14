import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello 123')

class PostUpdate(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('This should be a post (I mean GET) from browser')
    def post(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('success POST, i think from gmail')

class Watch(webapp2.RequestHandler);
    def post(self):
      

app = webapp2.WSGIApplication([
    ('/post123', PostUpdate),
    ('/', MainPage)
], debug=True)