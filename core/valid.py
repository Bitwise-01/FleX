# Date: 10/21/2017
# Author: Ethical-H4CK3R
# Description: Validates UserInput

class Valid(object):
 ''' Validates UserInput '''

 def checkName(self, name):
  if not name.isalpha():
   print '[-] Error: A name must be a string, and should not have any extensions'
   return 
  return True

 def checkID(self, num):
  if not num.isdigit():
   print '[-] Error: ID must be an interger'
   return   
  num = eval(num)
  if any([num>len(self.botnet), num-1<0]):
   print '[-] Error: ID not found'
   return 
  return True

 def checkIP(self, ip):
  try:
   if any([len(ip.split('.')) != 4, 
    not all([True if all([_.isdigit(), all([eval(_) >= 0, 
    eval(_) <= 255])]) else False for _ in ip.split('.')])]): 
    print '[-] Error: Please enter a valid IP';return
   return True
  except:print '[-] Error: Please enter a valid IP'   

 def checkPORT(self, port):
  if not port.isdigit():
   print '[-] Error: Please enter a valid PORT'
   return

  if any([eval(port)<0, eval(port)>65535]):
   print '[-] Error: Please enter a valid PORT'
   return 
  return True

 def checkArg(self, arg, num=None, min=None):
  n = len(arg)   
  if min:
   if min > n:
    print '[-] Error: This Function takes at least {} arguments ({} given)'.format(min, n)
    return
   return True
  if n != num:
   print '[-] Error: This Function takes {} arguments ({} given)'.format(num, n)
   return 
  return True
