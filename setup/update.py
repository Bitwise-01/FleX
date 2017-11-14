# Date: 10/25/2017
# Author: Ethical-H4CK3R
# Description: Updates & Upgrades Kali Linux

class Update(object):
 ''' Updates & Upgrades Kali Linux '''

 def __init__(self):
  self.sources = '/etc/apt/sources.list'
  self.repo = 'deb http://http.kali.org/kali kali-rolling main contrib non-free'

 def rewrite(self):
  with open(self.sources, 'w') as source:source.write(self.repo)


