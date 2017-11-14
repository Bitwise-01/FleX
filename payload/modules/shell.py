# Date: 10/08/2017
# Author: Ethical-H4CK3R
# Description: Shell

import os

class Shell(object):
 def __init__(self):
  self.home = os.path.expanduser('~')

 def cd(self, path=None):
  try:os.chdir(path if path else self.home)
  except:pass

 def exe(self, cmd):
  try:
   inpt, outpt, err = os.popen3(cmd)
   return '{}{}'.format(outpt.read(), err.read())  
  except:pass

 def CMD(self, CMD): 
  cmd = CMD.split()
  if cmd[0] == 'cls':
   return '0'
  if cmd[0] == 'cd': 
   if len(cmd) != 1:
    self.cd(' '.join(cmd[1:]))
   else:self.cd()
   return '0'   
  else:
   return self.exe(CMD)
