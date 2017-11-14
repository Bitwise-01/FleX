# Date: 09/23/2017
# Author: Ethical H4CK3R
# Description: Return System Info

from getpass import getuser
from platform import system, release, version, architecture, machine

system = {
   'System': system(),
   'Release': release(),
   'Version': version(),
   'Machine': machine(),
   'Username': getuser(),
   'Architecture': architecture()[0]
  }
