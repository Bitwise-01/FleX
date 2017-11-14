# Date: 10/24/2017
# Author: Ethical-H4CK3R
# Description: Install Wine & Requirements

from wine import Wine
from update import Update
from subprocess import Popen

class Install(object):
 ''' Install Required Software '''

 def __init__(self):
  self.required = ['mss', 'cmd2', 'requests']
  
 def update(self):
  Popen('clear'.split()).wait()
  print 'Updating System ...'
  Update().rewrite()
  Popen('apt-get update -qq', shell=True).wait()
  Popen('clear'.split()).wait()
  print 'Upgrading System ...\n\n'
  Popen('apt-get dist-upgrade -y', shell=True).wait()  

 def installPyReqs(self):
  for _ in self.required:
   Wine().installRequired(_)
   Popen('pip install {}'.format(_), shell=True).wait()   

 def run(self):
  self.update()
  Wine().install()
  self.installPyReqs()  
  Popen('clear'.split()).wait()
  print '[+] All Done'

if __name__ == '__main__':
 try:Install().run()
 except:print '\n[!] Error: Failed To Install Requirements'
