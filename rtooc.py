# rtoo main module providing methods for 
# actions

from subprocess import call


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
  


class IPT:
  def MarkPacket(self,iptables_object):
    self.iptables_object = iptables_object
    command1 = ['iptables','-t','mangle','-A','RTOO_POSTROUTING','-d',self.iptables_object,'-j','MARK','--set-mark','8']
    command2 = ['iptables','-t','mangle','-A','RTOO_POSTROUTING','-s',self.iptables_object,'-j','MARK','--set-mark','8']
    call(command1)
    call(command2)
  #def SetTrafficClass(self,bandwidth):
  #  self.bandwidth = bandwidth
        
   
     
    
