from google.appengine.ext import ndb

class Event(ndb.Model): #change Meme part to our choosing
    name = ndb.StringProperty(required=True)#change to date
    short_description = ndb.StringProperty(required=True)#change area
    date = ndb.DateProperty(required=True)#change time
    age_range = ndb.StringProperty(required=False)#change category
    location = ndb.StringProperty(required=True)
    




class Event_User(ndb.Model): #event user
  first_name = ndb.StringProperty()
  last_name = ndb.StringProperty()
  email = ndb.StringProperty()
   #type of events 
