import webapp2
import jinja2
import os
#from models import Meme, CssiUser ////importatn put our model EventUser
from google.appengine.api import users


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def checkLoggedInAndRegistered(request):
    # Check if user is logged in
    
    user = users.get_current_user()
        
    if not user: 
        request.redirect("/login") #ask to login,if not redirect 
        return
        welcome_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(welcome_template.render())
    
#class Upcoming(webapp2.RequestHandler):
    
    
    
    
    
#class AddEvents(webapp2.RequestHandler):

    
    # Check if user is registered
       
    email_address = user.nickname()
    registered_user = CssiUser.query().filter(CssiUser.email == email_address).get() #EventUser
    

    if not registered_user:
         request.redirect("/register") #useful if not registered goes to rdr
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
        
        meme = Meme(
            line1=self.request.get('user-first-ln'), 
            line2=self.request.get('user-second-ln'),
            owner=user.nickname(),
            img_choice=self.request.get('meme-type')
        )
        meme_key = meme.put()
        self.response.write("Meme created: " + str(meme_key) + "<br>")
        self.response.write("<a href='/allmemes'>All memes</a> | ")
        self.response.write("<a href='/usermemes'>My memes</a>")
        


class AllMemesHandler(webapp2.RequestHandler):
    def get(self):
        checkLoggedInAndRegistered(self)
        
        
        
        all_memes = Meme.query().fetch() #modify
        
        the_variable_dict = {
            "all_memes": all_memes
        }
        
        all_memes_template = the_jinja_env.get_template('templates/all_memes.html')
        self.response.write(all_memes_template.render(the_variable_dict))

class UserMemesHandler(webapp2.RequestHandler): #imporatnt line 137 keeps user stuff
    def get(self):
        checkLoggedInAndRegistered(self)
        
        user = users.get_current_user()
        email_address = user.nickname()
        
        user_memes = Meme.query().filter(Meme.owner == email_address).fetch() #modify get stored in user names
        
        the_variable_dict = {
            "user_memes": user_memes
        }
        
        user_memes_template = the_jinja_env.get_template('templates/user_memes.html') #redirects
        self.response.write(user_memes_template.render(the_variable_dict))
   
        

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        
        login_template = the_jinja_env.get_template('templates/login.html') #this will be loaded first
        the_variable_dict = {
            "login_url":  users.create_login_url('/')
        }
        
        self.response.write(login_template.render(the_variable_dict))
        

class RegistrationHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        
        registration_template = the_jinja_env.get_template('templates/registration.html') #rdr
        the_variable_dict = {
            "email_address":  user.nickname()
        }
        
        self.response.write(registration_template.render(the_variable_dict))
#class Calendar(webapp2)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
>>>>>>> f73ee8a691b92dfb6bf2043bd1fec601d25e9d36
    
    def post(self):
        user = users.get_current_user()
        
        #Create a new CSSI User in our database
        
        cssi_user = CssiUser(
            first_name=self.request.get('first_name'), 
            last_name =self.request.get('last_name'), 
            email=user.nickname() # modify for our use
        )
        
        cssi_user.put()
        
        self.response.write('Thanks for signing up, %s! <br><a href="/">Home</a>' %
        cssi_user.first_name)
        
                  
    
app = webapp2.WSGIApplication([
<<<<<<< HEAD
    ('/', HomeHandler),
    ('/allmemes', AllMemesHandler), 
    ('/usermemes', UserMemesHandler), #line 83
    ('/login', LoginHandler), # should use this rdr
    ('/register', RegistrationHandler)# should use this rdr
], debug=True)
=======
    ('/', EnterInfoHandler)
], debug=True)

>>>>>>> f73ee8a691b92dfb6bf2043bd1fec601d25e9d36
