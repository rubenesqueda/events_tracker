import webapp2
import jinja2
import os
from models import Event, Event_User 
from google.appengine.api import users
from google.appengine.ext import ndb


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def checkLoggedInAndRegistered(request):
    # Check if user is logged in
    user = users.get_current_user()
        
    if not user: 
        request.redirect("/sign_in") #ask to login,if not redirect 
        return 
    
    # Check if user is registered
       
    email_address = user.nickname()
    registered_user = Event_User.query().filter(Event_User.email == email_address).get() 
    

    if not registered_user:
         request.redirect("/signup") #useful if not registered goes to rdr
         return 


def isRegistered():
    user = users.get_current_user()
        
    # Check if user is registered
       
    email_address = user.nickname()
    registered_user = Event_User.query().filter(Event_User.email == email_address).get() 
    
    return registered_user
    
#class Map(webapp2.RequestHandler):
    
    

class HomePageHandler(webapp2.RequestHandler):
    def get(self):  

        the_variable_dict = {
            "logout_url":  users.create_logout_url('/'),
            "login_url": users.create_login_url('/signup')
        }
        
        welcome_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(welcome_template.render(the_variable_dict))

    def post(self):
        checkLoggedInAndRegistered(self)
        
        user = users.get_current_user()
        
        event = Event(
            name=self.request.get('event-name'), 
            short_description=self.request.get('short-description'),
            date=self.request.get('event-date'),
            age_range=self.request.get('age-range'),
            location=self.request.get('event-location')
            
        )
        event_key = event.put()
        self.response.write("Meme created: " + str(event_key) + "<br>")
        self.response.write("<a href='/upcoming'>All Events</a> | ")
        self.response.write("<a href='/user_events'>My events</a>")
        


class UpcomingHandler(webapp2.RequestHandler):
    def get(self):
        checkLoggedInAndRegistered(self)
        
        
        
        all_events = Event.query().fetch() #modify
        
        the_variable_dict = {
            "all_events": all_events
        }
        
        all_memes_template = the_jinja_env.get_template('templates/upcoming.html')
        self.response.write(all_memes_template.render(the_variable_dict))

class UserEventsHandler(webapp2.RequestHandler): #imporatnt line 137 keeps user stuff
    def get(self):
        checkLoggedInAndRegistered(self)
        
        user = users.get_current_user()
        email_address = user.nickname()
        
        user_events = Event.query().filter(Event.owner == email_address).fetch() #modify get stored in user names
        
        the_variable_dict = {
            "user_events": user_events
        }
        
        user_memes_template = the_jinja_env.get_template('templates/user_events.html') #redirects
        self.response.write(user_memes_template.render(the_variable_dict))
   
        

class AddEventsHandler(webapp2.RequestHandler):
    def get(self):
        add_template = the_jinja_env.get_template('templates/add_events.html')
        self.response.write(add_template.render())



class SignInHandler(webapp2.RequestHandler):
    def get(self):
        checkLoggedInAndRegistered(self)
        login_template = the_jinja_env.get_template('templates/signin.html') #this will be loaded first
        the_variable_dict = {
            "login_url":  users.create_login_url('/signup')
        }
        
        self.response.write(login_template.render(the_variable_dict))
        

class SignUpHandler(webapp2.RequestHandler):
    def get(self):
        if isRegistered():
            self.redirect("/")
            return
            
        the_variable_dict = {
            "logout_url":  users.create_logout_url('/')
        }
        
        welcome_template = the_jinja_env.get_template('templates/registration.html')
        self.response.write(welcome_template.render(the_variable_dict))
        
        
        
    def post(self):
        #checkLoggedInAndRegistered(self)
        
        user = users.get_current_user()
        event_user = Event_User(
            first_name=self.request.get('first_name'), 
            last_name =self.request.get('last_name'), 
            email=user.nickname() # modify for our use
        )
        
        event_user.put()
        
        self.response.write('Thanks for signing up, %s! <br><a href="/">Home</a>' %
        event_user.first_name)
        # event = Event(
        #     name=self.request.get('event-name'), 
        #     date=self.request.get('event-date'),
        #     location=self.request.get('event-location'),
        #     description=self.request.get('short-description'),
        #     age_range=self.request.get('age-range')
        # )
        # event_key = event.put()
        # self.response.write("Meme created: " + str(event_key) + "<br>")
        # self.response.write("<a href='/allmemes'>All memes</a> | ")
        # self.response.write("<a href='/usermemes'>My memes</a>")
    #     checkLoggedInAndRegistered(self)
    #     user = users.get_current_user()
    #     registration_template = the_jinja_env.get_template('templates/registration.html') #rdr
    #     the_variable_dict = {
    #         "email_address":  user.nickname()
    #     }
        
    #     self.response.write(registration_template.render(the_variable_dict))
    #     #class Calendar(webapp2)
    
    # def post(self):
    #     user = users.get_current_user()
        
    #     #Create a new CSSI User in our database
        
    #     event_user =Event_User(
    #         first_name=self.request.get('first_name'), 
    #         last_name =self.request.get('last_name'), 
    #         email=user.nickname() # modify for our use
    #     )
        
    #     Event_User.put()
        
    #     self.response.write('Thanks for signing up, %s! <br><a href="/">Home</a>' %
    #     event_user.first_name)
        
                  
    
app = webapp2.WSGIApplication([
    ('/', HomePageHandler),
    ('/upcoming', UpcomingHandler),
    ('/add_events', AddEventsHandler),
    #('/maps', MapsHandler),
    ('/user_events', UserEventsHandler), #line 83
    ('/sign_in', SignInHandler), # should use this rdr
    ('/signup', SignUpHandler)# should use this rdr
], debug=True)


