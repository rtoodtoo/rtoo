#!/usr/bin/python

import cmd
import sys,shlex
import os,re
import rtooc
import helpc
import dbconn

RtooVersion="0.1b"

m = dbconn.mycon()
conn = m.conn

class CLI(cmd.Cmd,rtooc.IPT,rtooc.TC,helpc.helpc):
 
    def __init__(self):
        cmd.Cmd.__init__(self)
        print "Initializing Rtoo",RtooVersion,"\n",
        print "For command reference, type help\n"
        self.prompt = 'rtoo> '

    def emptyline(self):
      pass

 

    def do_set(self,command_args):
      
      try:
        arg_count=len(shlex.split(command_args))    
        arg=shlex.split(command_args)
      except ValueError:
        return self.help_error()
 
      #If no argument is provided, display help
      if arg_count <= 1:
        return self.help_set()

      #First argument is pool
      if arg[0] == "pool":
        #Check if arguments are provided,if not display help 
        try:
          self.pool_name = arg[1] 
          self.bandwidth = arg[2]
        except IndexError:
          return self.help_set()

        #Set pool and add it into conf.ini file  
        if self.SetTrafficPool(self.bandwidth) == 0:
          #TC returns 0 only if it is successful
          print "Pool : %s" % (self.pool_name)
          print "Bandwidth: %s" % (self.bandwidth) 
          print "Added successfully"
          cursor = conn.cursor()
          cursor.execute ("INSERT INTO pool (pool_id,pool_name,bandwidth,comment) VALUES (null,%s,%s,'no_comment')",(self.pool_name,self.bandwidth))
          cursor.close()
        else:
          print "An error occured during pool allocation"
      
      #Firt argument is address, it is a name for network address
      #and must be in conf.ini file
      if arg[0] == "bandwidth":
        try:
          self.address_name = arg[1]
          self.network = arg[2]
          self.bandwidth = arg[3]
          self.pool_name = arg[4]
          self.exceed = arg[5]
        except (IndexError,ValueError):
          return self.help_set() 
      
       ##FIXME: Check pool existence before BW setting
       ##Checks: bandwidth,network,address_name for proper format
       ##       
       
      if re.search(r'\W+',self.address_name):
         print "Address name cannot have non-alpanumeric characters"
         return self.help_shell() 
      if not re.search(r'^\d+(kbit|Mbit)$',self.bandwidth):
         print self.bandwidth
         print "Bandwidth format is incorrect"
         return self.help_shell()

       #cursor = conn.cursor()
       #cursor.execute ("INSERT INTO bandwidth (address_id,address_name,network,bandwidth,exceed,comment) VALUES (null,%s,%s,'no_comment')",(self.pool_name,self.bandwidth))
       #cursor.close() 

    def do_quit(self, arg):                                                                                
        sys.exit(1)     
    # shortcuts
    do_q = do_quit

cli = CLI()
cli.cmdloop()
