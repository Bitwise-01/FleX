# Date: 10/26/2017
# Author: Ethical-H4CK3R
# Description: Prompt

import os
from platform import node

class Prompt(object):
 ''' A nice looking prompt '''

 def __init__(self):
  # colors
  self.n = '\033[0m'
  self.b = '\033[94m'
  self.r = '\033[91m'

 def getprompt(self, name=node(), host=os.getlogin(), shell=False):
  dirs = os.getcwd().replace(os.path.expanduser('~'), '') 
  return '{}{}@{}{}::{}~{}{}# '.format(self.r, host,
                                        name, self.n, 
                                        self.b, dirs, 
                                        self.n) if not shell else '{}{}@{}{}::# '.format(self.r, name, host, self.n)



  
