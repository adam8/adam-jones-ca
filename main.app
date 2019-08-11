import webapp2

class MainHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write("hello! adamjones on app engine from codesandbox via github. Test!")

    app = webapp2.WSGIApplication([
      ('/', MainHandler)
    ], debug=True)