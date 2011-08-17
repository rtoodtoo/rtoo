#!/usr/bin/python

import MySQLdb
import sys

hostname = "localhost"
username = "rtoo"
password = "rtoo"
db = "rtoo"


class mycon:
#Connect to DB
  def __init__(self):
    try:
      self.conn = MySQLdb.connect ( host = hostname,
                           user = username,
                           passwd = password,
                           db = db)
    except MySQLdb.Error,e:
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)
