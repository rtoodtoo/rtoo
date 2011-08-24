#Documentation container for command help

class helpc:

    def help_set(self):                                                                                   
        print "syntax: set {options}"                                                                       
        print """USAGE:                                                                                  
        set pool {pool_name} bandwidth {rate} [comment]
        set pool {pool_name} status [remove|inactive|active]      
        set member {member_name} {network} {rate} [remove|inactive|active] [comment]
        set assign {member_name} {pool_name} [exceed|no-exceed]

        
        [HELP]
        >pool: creates a new pool
          pool_name: the new of the pool
            >bandwidth: To set a bandwidth limit on specified rate
                 rate: the rate in kbit or Mbit e.g 128kbit or 2Mbit
            >status: Modifies status of pool            
                 *remove: removes the pool from bandwidth management system along with ALL connected members!!!
                 *inactive: temporarily make this pool inactive by which ALL members using this pool will have no traffic shaping
                 *active: activates an inactive pool which activates shaping in all connected members 
        
        >assign: sets bandwidth for a specific network in units kbit or Mbit and binds it into a shared pool
                        *member: name to identify this specific network only alphanumeric characters allowed
                        *network: Network address in notation 192.168.1.0/24
                        *bandwidth: the rate in kbit or Mbit e.g 128kbit or 2Mbit
                        *pool_name: the pool that this network range is bound to 
                        *exceed: If set, user can exceed its link speed upto the pool it is bound to
                        *no-exceed: If set, user cannot exceed its link speed defined
                        *comment: optional argument to keep some information for the admin

         >member: performs operation on specified member
                *member_name: the member which should be changed
                    *network: Network address in notation 192.168.1.0/24
                    *remove: removes the member from bandwidth management system!!!
                    *inactive: temporarily makes traffic shaping inactive 
                    *active: enables shaping back  


        [EXAMPLE COMMANDS]

        set pool Engineering 2Mbit
        set pool Students 512Kbit
        set pool Engineering inactive
        set member John 192.168.10.1/32 128kbit
        set bandwidth John Engineering no-exceed
        set bandwidth Bob Students exceed
        """                                                                                                
    def help_show(self):
        print "syntax: show {options}"
        print """USAGE:
        show traffic {pool|member} [pool_name|member_name]
        show conf 

        [HELP]
        traffic: display active flowing traffic for the specified entity
                 >pool: to show traffic in pool
                     *pool_name: name of the pool 
                 >member: to show traffic for a specific network
                     *member_name: name of a registered member in rtoo
        
        conf : shows the active configuration made so far 
        
        [EXAMPLE COMMANDS]:
        show traffic name John
        show traffic name all
        show traffic pool Engineering
        """
                 
        
          

    def help_error(self):
        print "Please check your input as it contains errors"
        print "" 

    def help_shell(self):
        pass
                                                                                                           
    def help_quit(self):                                                                                   
        print "syntax: quit",                                                                              
        print "-- terminates the application"         
