import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<html><body><div className="App"><div><h1>Adam Skye Jones</h1><p>Feet on the ground,<br />Head in the cloud</p></div></div></body></html>')

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
