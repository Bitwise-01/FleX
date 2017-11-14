# Date: 10/23/2017
# Author: Ethical-H4CK3R
# Description: Returns True if the file compiled & moved

import os

class FileState(object):
 ''' Returns True if the file compiled & moved OR if the file is not compiled '''

 @staticmethod
 def isCompiled(exe):
  name = exe.split(os.path.sep)[-1]
  return False if all([name[:6].lower() == 'python',
   any([os.path.splitext(name)[1] == '.exe',  
        not os.path.splitext(name)[1]])]) else True
   
 @classmethod
 def isMoved(cls, exe):
  dirname = os.path.dirname(os.path.realpath(exe))  
  return True if any([not cls.isCompiled(exe), 
   not all([os.path.basename(dirname) != 'SystemUpdate',
    len(dirname.split(os.path.sep)) != 2])]) else False
