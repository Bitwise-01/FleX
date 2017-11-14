# Date: 10/21/2017
# Author: Ethical-H4CK3R
# Description: A Shell Between Bot & Master

import time
import socket
import threading

class Shell(object):
 ''' Shell Console '''

 def __init__(self, bot):
  self.bot = bot
  self.wait = False
  self.alive = True
  self.session = bot.session
 
 def receiver(self):
  while self.alive:
   try:
    cmdOutput = self.session.recv(1024)
    if not cmdOutput:
     self.alive = False
     self.wait = False

    output = cmdOutput.replace('\n', '')    
    if output.isdigit():pass
    else:print cmdOutput
    self.wait = False
   except:pass
   
 def run(self, prompt):
  threading.Thread(target=self.receiver).start() 
  while self.alive:
   try:
    cmd = raw_input('{}'.format(prompt))
    if not cmd.strip().replace('\n', ''):continue
    self.session.sendall(cmd)
    self.wait = True
    [time.sleep(1) for _ in range(5) if self.wait and self.alive]
    self.wait = False
   except KeyboardInterrupt:
    print 
    try:self.session.sendall('exit')
    finally:self.alive = False
   except socket.error:
    self.dead.put(self.bot)
    self.alive = False
   except:pass
