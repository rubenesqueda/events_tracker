import webapp2
import jinja2
import os
from models import Event, CssiUser 
from google.appengine.api import users


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
        welcome_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(welcome_template.render())
    
#class Upcoming(webapp2.RequestHandler):
    
    
    
    
    
#class AddEvents(webapp2.RequestHandler):

    
    # Check if user is registered
       
    email_address = user.nickname()
    registered_user = Event_User.query().filter(Event_User.email == email_address).get() 
    

    if not registered_user:
         request.redirect("/signup") #useful if not registered goes to rdr
         return 

    
#class Map(webapp2.RequestHandler):
    
    

class HomePage(webapp2.RequestHandler):
    def get(self):  
        checkLoggedInAndRegistered(self)
        
        the_variable_dict = {
            "logout_url":  users.create_logout_url('/')
        }
        
        welcome_template = the_jinja_env.get_template('templates/home.html')
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
            "all_memes": all_events
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
            "user_memes": user_events
        }
        
        user_memes_template = the_jinja_env.get_template('templates/user_memes.html') #redirects
        self.response.write(user_memes_template.render(the_variable_dict))
   
        

class AddEventsHandler(webapp2.RequestHandler):
    def get(self):
        add_template = the_jinja_env.get_template('templates/add_events.html')
        self.response.write(add_template.render())



class SignInHandler(webapp2.RequestHandler):
    def get(self):
        
        login_template = the_jinja_env.get_template('templates/login.html') #this will be loaded first
        the_variable_dict = {
            "login_url":  users.create_login_url('/')
        }
        
        self.response.write(login_template.render(the_variable_dict))
        

class SignUpHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        
        registration_template = the_jinja_env.get_template('templates/registration.html') #rdr
        the_variable_dict = {
            "email_address":  user.nickname()
        }
        
        self.response.write(registration_template.render(the_variable_dict))
#class Calendar(webapp2)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    def post(self):
        user = users.get_current_user()
        
        #Create a new CSSI User in our database
        
        event_user = Event_User(
            first_name=self.request.get('first_name'), 
            last_name =self.request.get('last_name'), 
            email=user.nickname() # modify for our use
        )
        
        Event_User.put()
        
        self.response.write('Thanks for signing up, %s! <br><a href="/">Home</a>' %
        event_user.first_name)
        
                  
    
app = webapp2.WSGIApplication([

    ('/', HomePage),
    ('/upcoming', UpcomingHandler),
    ('/add_events', AddEventsHandler),
    #('/maps', MapsHandler),
#    ('/calendar' CalendarHandler),
    ('/user_events', UserEventsHandler), #line 83
    ('/sign_in', SignInHandler), # should use this rdr
    ('/signup', SignUpHandler)# should use this rdr
], debug=True)


