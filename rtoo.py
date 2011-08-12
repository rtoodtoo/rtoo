#!/usr/bin/python

import cmd
import sys,shlex
import os,ConfigParser
import rtooc
from helpc import *

RtooVersion="0.1b"

#Fetch configuration items
config = ConfigParser.RawConfigParser()
config.read('settings.ini')

#print config.get('INTERFACE','WAN')


class CLI(cmd.Cmd,rtooc.IPT,helpc):

    def __init__(self):
        cmd.Cmd.__init__(self)
        print "Initializing Rtoo",RtooVersion,"\n",
        print "For command reference, type help\n"
        self.prompt = 'rtoo> '


    def emptyline(self):
      pass

    def do_setbw(self,iptables_object):
      
      ipt=rtooc.IPT()
      #Mark packet in iptables mangle table
      ipt.MarkPacket(iptables_object)
      #define traffic class in TC subsystem
        

   

    def do_quit(self, arg):                                                                                
        sys.exit(1)     
    # shortcuts
    do_q = do_quit

cli = CLI()
cli.cmdloop()
