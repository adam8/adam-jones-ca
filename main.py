import webapp2
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello 123. CodeSandBox.io')

class PostUpdate(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('This should be a post (I mean GET) from browser')
    def post(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('success POST, i think from gmail')

class Watch(webapp2.RequestHandler):
  def get(self):
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        self.response.write('No labels found.')
    else:
        for label in labels:
            self.response.write(label['name'])

app = webapp2.WSGIApplication([
    ('/post123', PostUpdate),
    ('/watch', Watch),
    ('/', MainPage)
], debug=True)
