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
  
     
    def error_msg(self,error):
      """To stop processing and printing error"""  
      self.error = error
      print ""
      print "ERROR: "+self.error
      print ""

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
          self.pool_option = arg[2]
          self.pool_option_value = arg[3]
        except IndexError:
          return self.help_set()
       
        #At this stage we can check if the pool name exists already
        cursor = conn.cursor()
        cursor.execute("SELECT pool_name from pool where pool_name=%s LIMIT 1",(self.pool_name))
        if cursor.rowcount !=0:
          return self.error_msg("Pool name is already defined")
 
        #Comment is optional,be sure it doesn't cause problem
        try:
          self.comment = arg[4]
        except IndexError:
          self.comment = None 

        #Option to pool argument is bandwidth
        if self.pool_option == 'bandwidth':
           #We expect the rate in kbits and Mbits in here
           self.rate =  self.pool_option_value
           if self.SetTrafficPool(self.rate) == 0:
             #TC returns 0 only if it is successful
             print "Pool : %s" % (self.pool_name)
             print "Bandwidth: %s" % (self.rate) 
             print "Added successfully"
             if not self.comment: 
               self.comment = ""
             cursor = conn.cursor()
             cursor.execute ("INSERT INTO pool (pool_id,pool_name,bandwidth,comment) VALUES (null,%s,%s,%s)",(self.pool_name,self.rate,self.comment))
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
