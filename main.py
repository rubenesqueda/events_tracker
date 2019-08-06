import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):
        
        welcome_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(welcome_template.render())
    
class Upcoming(webapp2.RequestHandler):
    
    
    
    
    
class AddEvents(webapp2.RequestHandler):
    
    
    
class Map(webapp2.RequestHandler):
    
    


class Calendar(webapp2)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler)
], debug=True)
=======
>>>>>>> f851e6301e5102c66197212d7c53c671a9afdb53
