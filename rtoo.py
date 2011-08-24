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
      
    
      ####MEMBER BEGIN####
      if arg[0] == "member":
        #Check option existence
        try:
          self.member_name = arg[1]
          self.network = arg[2]
          self.rate = arg[3]
          #remove,inactive,active
          self.state = arg[4]
        except IndexError:
          return self.help_set()
        
        #Comment is optional
        try:
          self.comment = arg[4]
        except IndexError:
          self.comment = None
        #TODO: created/modify member table according to the structure
         
                  

 
      #Firt argument is address, it is a name for network address
      #and must be in conf.ini file
      if arg[0] == "assign":
        try:
          self.member_name = arg[1]
          self.pool_name = arg[2]
          self.exceed = arg[3]
        except (IndexError,ValueError):
          return self.help_set() 
      
        ##FIXME: There is a flaw in this regex, check once again 
        if re.search(r'\W+',self.member_name):
           print "Member name cannot have non-alpanumeric characters"
           return self.help_shell() 
        if not re.search(r'^\d+(kbit|Mbit)$',self.bandwidth):
           print self.bandwidth
           print "Bandwidth format is incorrect"
           return self.help_shell()

        #Pool should be in place if this command is issued, check pool existence
        cursor = conn.cursor() 
        cursor.execute("SELECT * from pool where pool_name=%s",(self.pool_name))
        cursor.close()
        if cursor.rowcount==0:
          return self.error_msg("Specified pool name doesn't exist, please set the pool name first using 'set pool' command")
  


       #cursor = conn.cursor()
       #cursor.execute ("INSERT INTO bandwidth (address_id,address_name,network,bandwidth,exceed,comment) VALUES (null,%s,%s,'no_comment')",(self.pool_name,self.bandwidth))
       #cursor.close() 

    def do_quit(self, arg):                                                                                
        sys.exit(1)     
    # shortcuts
    do_q = do_quit

cli = CLI()
cli.cmdloop()
