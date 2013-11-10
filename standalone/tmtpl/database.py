#!/usr/bin/env python
#

#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

class Sewdb:
    def __init__(self, adbhost="mysql.sewbuzzed.com", adbuser="seamly", adbpass="seamlypass4u", adbname="sewbuzzed_pdb"):
        self.dbhost = adbhost
        self.dbuser = adbuser
        self.dbpass = adbpass
        self.dbname = adbname
        self.con = None
        return

    # open
    #
    def open(self):
        self.con = mdb.connect(self.dbhost, self.dbuser, self.dbpass, self.dbname);
        return

    # doquery
    #
    def doquery(self, query):
        #print query
        self.con.query(query)
        return

    def docommit(self):
        return self.con.commit()

    def insertid(self):
        return self.con.insert_id()

    def store_result(self):
        return self.con.store_result()        

    # dumpinfo
    #
    def dumpinfo(self):
        print "dbhost = ", self.dbhost
        print "dbuser = ", self.dbuser
        print "dbpass = ", self.dbpass
        print "dbname = ", self.dbname

# vi:set ts=4 sw=4 expandtab syntax=python:
