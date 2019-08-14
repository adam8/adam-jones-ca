import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello again from my phone, World!')

class PostUpdate(webapp2.RequestHandler):
    def post(self);
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('This should be a post from gmail')

app = webapp2.WSGIApplication([
    ('post', postUpdate),
    ('/', MainPage),
], debug=True)