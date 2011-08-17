#Documentation container for command help

class helpc:

    def help_set(self):                                                                                   
        print "sytax: set {arguments}"                                                                       
        print """usage:                                                                                  
        pool {name} {bandwidth}      
        bandwidth {name} {network} {bandwidth} {pool_name} {exceed|no-exceed} [comment]
        
        pool: assigns bandwidth to a pool defined 
        bandwidth:   sets bandwidth for a specific network and ties it into shared pool
                     >name: string to identify this specific network only alphanumeric characters allowed
                     >network: Network address in notation 192.168.1.0/24
                     >bandwidth: the rate in kbit or Mbit e.g 128kbit or 2Mbit
                     >pool_name: the pool that this network range is bound to 
                     >exceed: If set, user can exceed its link speed upto the pool it is bound to
                     >no-exceed: If set, user cannot exceed its link speed defined
                     >comment: optional to keep some information for the admin


        Example commands:

        set pool Engineering 2Mbit
        set pool Students 512Kbit
        set bandwidth John 192.168.10/32 128kbit Engineering no-exceed
        set bandwidth Bob 192.168.2.20/32 64kbit Students exceed
        """                                                                                                

    def help_error(self):
        print "Please check your input as it contains errors"
        print "" 

    def help_shell(self):
        pass
                                                                                                           
    def help_quit(self):                                                                                   
        print "syntax: quit",                                                                              
        print "-- terminates the application"         
