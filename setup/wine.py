# Date: 10/14/2017
# Author: Ethical-H4CK3R
# Description: Installs Wine

import os
import sys
import urllib2
import subprocess

class Wine(object):
 def __init__(self):
  self.pyVer = '2.7.14'  # only 2.7
  self.wine = '/root/.wine'
  self.pip = 'https://bootstrap.pypa.io/get-pip.py'
  self.python = 'https://python.org/ftp/python/{0}/python-{0}.msi'.format(self.pyVer)
  
 def installWine(self):
  subprocess.Popen('clear'.split()).wait()
  print 'Installing Wine ...'
  subprocess.Popen('sudo dpkg --add-architecture i386 &&\
                   sudo apt-get update -qq&&\
                   sudo apt-get install wine wine64 wine32 -y -qq', shell=True).wait()

 def downloadPip(self):
  subprocess.Popen('clear'.split()).wait()
  print '\nDownloading PIP ...'
  self.pip = urllib2.urlopen(self.pip).read()
  self.savePip()

 def savePip(self):
  print 'Download Completed\n'
  with open('get-pip.py', 'w') as pip:
   pip.write(self.pip)
  self.installPip()

 def downloadPython(self):
  subprocess.Popen('clear'.split()).wait()
  print '\nDownloading Python ...'
  self.python = urllib2.urlopen(self.python).read()
  self.savePython()

 def savePython(self):
  print 'Download Competed\n'
  with open('python-{}.msi'.format(self.pyVer), 'wb') as f:
   f.write(self.python)
  self.installPython()

 def installPython(self):
  subprocess.Popen('wine msiexec /i python-{}.msi'.format(self.pyVer), shell=True).wait()

 def installPip(self):
  if not os.path.exists(self.wine):
   sys.exit('Error: Unable to locate wine')
  subprocess.Popen('wine {}/drive_c/Python27/python.exe\
                   get-pip.py'.format(self.wine), shell=True).wait()

 def installPyinstaller(self):
  subprocess.Popen('clear'.split()).wait()
  print '\nInstalling Pyinstaller ...\n'
  subprocess.Popen('wine {}/drive_c/Python27/python.exe\
                   -m pip install pyinstaller'.format(self.wine), shell=True).wait()

 def installRequired(self, name):
  subprocess.Popen('clear'.split()).wait()
  print '\nInstalling {}'.format(name.title())
  subprocess.Popen('wine {}/drive_c/Python27/python.exe\
                   -m pip install {}'.format(self.wine, name), shell=True).wait()

 def extra(self):
  subprocess.Popen('wine pyhook.exe', shell=True).wait()
  subprocess.Popen('wine pywin32.exe', shell=True).wait()

 def install(self):
  self.installWine()
  self.downloadPython()
  self.downloadPip()
  self.installPyinstaller() 
  self.extra()
  try:
   os.remove('get-pip.py')
   os.remove('python-{}.msi'.format(self.pyVer))
  except:pass
