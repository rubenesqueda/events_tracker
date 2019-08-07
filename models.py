from google.appengine.ext import ndb

class Meme(ndb.Model): #change Meme part to our choosing
    line1 = ndb.StringProperty(required=True)#change to date
    line2 = ndb.StringProperty(required=True)#change area
    owner = ndb.StringProperty(required=True)#change time
    img_choice = ndb.StringProperty(required=False)#change category

class CssiUser(ndb.Model): #event user
  first_name = ndb.StringProperty()
  last_name = ndb.StringProperty()
  email = ndb.StringProperty()
   #type of events 
