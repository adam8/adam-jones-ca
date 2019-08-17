import webapp2

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello 123. CodeSandBox.io?')

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
