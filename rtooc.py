# rtoo main module providing methods for 
# actions

#from subprocess import Popen,call
import subprocess 


class TC:
  """TC traffic control class"""
  def SetQdisc(self,interface):
    self.interface  = interface
    command = ['tc','qdisc','add','dev',self.interface,'root','handle','1:0','htb']
    call(command)
 
  def ShowQdisc(self,interface):
    self.interface = interface
    command = ['tc','qdisc','show','dev',self.interface]
    call(command)
  def DelQdisc(self,interface):
    self.interface = interface 
    command = ['tc','qdisc','del','dev',self.interface,'root','handle','1:0','htb']
    call(command)
  
  def SetTrafficPool(self,bandwidth):
    """This sets the branch class which will be a container for sub classes"""
    self.bandwidth = bandwidth
    command = ['tc','class','add','dev','eth1','parent','1:','classid','1:1','htb','rate',self.bandwidth,'ceil',self.bandwidth]
    #devnull = open('/dev/null','w')
    #return call(command)
    #subprocess.Popen(command,stdout = devnull,stderr = devnull)
    return subprocess.call(command)
    #return provides exit value to main program, returns 0 on success, 2 on error


class IPT:
  def MarkPacket(self,iptables_object):
    self.iptables_object = iptables_object
    command1 = ['iptables','-t','mangle','-A','RTOO_POSTROUTING','-d',self.iptables_object,'-j','MARK','--set-mark','8']
    command2 = ['iptables','-t','mangle','-A','RTOO_POSTROUTING','-s',self.iptables_object,'-j','MARK','--set-mark','8']
    call(command1)
    call(command2)
