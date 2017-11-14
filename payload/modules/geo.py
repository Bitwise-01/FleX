# Date: 09/23/2017
# Author: Ethical H4CK3R
# Description: Get the location of bot

import json
import requests

class Geolocate(object):	
 def __init__(self):
  self.url = 'http://ip-api.com/json'
  self.data = None
  self.location = {
                   'Ip': None, 
                   'Country': None, 
          
                   'City': None,
                   'State': None,

                   'Zipcode': None,
                   'Timezone': None,

                   'Latitude': None,
                   'Longitude': None
                  }
    
 def getGeo(self):
  try:
   response = requests.get(self.url)
   self.data = json.loads(response.text)   
   self.getInfo()
  except:return

 def getInfo(self):
  self.location['Ip'] = self.data['query']
  self.location['Country'] = self.data['country']

  self.location['City'] = self.data['city']
  self.location['State'] = self.data['regionName']

  self.location['Zipcode'] = self.data['zip']
  self.location['Timezone'] = self.data['timezone']

  self.location['Latitude'] = self.data['lat']
  self.location['Longitude'] = self.data['lon']
