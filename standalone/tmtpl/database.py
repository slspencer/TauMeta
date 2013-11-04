#!/usr/bin/env python
#

#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

class Sewdb:

    m_fields = [
        "customername",
        "units",
        "height",
        "nape_to_floor",
        "waist_to_floor",
        "hip_to_floor",
        "knee_to_floor",
        "ankle_to_floor",
        "head_and_neck_length",
        "midneck",
        "neck",
        "neck_diameter",
        "front_neck_width",
        "back_neck_width",
        "neck_height",
        "shoulder_length",
        "across_chest",
        "across_back",
        "highbust",
        "front_highbust_width",
        "front_highbust_height",
        "back_highbust_width",
        "back_highbust_height",
        "bust",
        "front_bust_width",
        "front_bust_height",
        "back_bust_width",
        "back_bust_height",
        "bust_point_distance",
        "side_bust_height",
        "lowbust",
        "front_lowbust_width",
        "front_lowbust_height",
        "front_lowbust_length",
        "back_lowbust_width",
        "waist",
        "front_waist_width",
        "front_waist_length",
        "back_waist_width",
        "back_waist_length",
        "side_waist_length",
        "front_neck_balance",
        "back_neck_balance",
        "front_shoulder_balance",
        "back_shoulder_balance",
        "front_waist_balance",
        "back_waist_balance",
        "highhip",
        "front_highhip_width",
        "front_highhip_height",
        "back_highhip_width",
        "back_highhip_height",
        "side_highhip_height",
        "hip",
        "front_hip_width",
        "front_hip_height",
        "back_hip_width",
        "back_hip_height",
        "side_hip_height",
        "armscye",
        "overarm_length",
        "underarm_length",
        "bicep",
        "armcap_height",
        "hand_length",
        "rise",
        "front_rise",
        "side_rise",
        "back_rise",
        "crotch_length",
        "front_crotch_length",
        "back_crotch_length",
        "front_crotch_extension",
        "back_crotch_extension",
        "outseam",
        "inseam",
        "thigh",
        "front_thigh_width",
        "back_thigh_width",
        "knee",
        "calve",
        "ankle",
        "foot"
    ]

    def __init__(self, adbhost="localhost", adbuser="seamly", adbpass="seamlypass", adbname="seamly_test_1"):
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
