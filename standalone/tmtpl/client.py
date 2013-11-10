#!/usr/bin/python
#
# Client data module
#
# This file is part of the tmtp (Tau Meta Tau Physica) project.
# For more information, see http://www.taumeta.org/
#
# Copyright (C) 2010, 2011, 2012 Susan Spencer and Steve Conklin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. Attribution must be given in 
# all derived works.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import json

from constants import *
from database import *
# Define globals

class ClientData(object):
    """
    Class used to store client data
    """
    def __init__(self):
        return

class Client(object):
    """
    Class to hold client-specific data
    Does unit conversions for cm or inches and returns data in pts
    """
    def __init__(self, filename, filetype= 'json'):
        # This is set up to be extensible for XML or other formats

        self.filetypes = ['json', 'database']
        self.data = ClientData()
        print "Client init filetype = ", filetype
        if filetype not in self.filetypes:
            print 'Client: supported file types are ', self.filetypes
        if filetype == 'json':
            self.__readJson__(filename)
        elif filetype == 'database':
            self.__readDb__(filename)

    def __readJson__(self, datafilename):
        self.info={}

        # open the client file and read data
        f = open(datafilename, 'r')
        self.client = json.load(f)
        f.close()

        # Check to make sure we have units
        try:
            units = self.client['measureunit']['value']
            if units == 'cm':
                #self.__conversion__ = cm_to_pt
                self.__conversion__ = CM_TO_PX
            elif  units == 'in':
                #self.__conversion__ = in_to_pt
                self.__conversion__ = IN_TO_PX
        except KeyError:
            print 'Client Data measurement units not defined in client data file'
            raise

        # read everything into attributes
        for key, val in self.client.items():
            if len(key.split('.')) > 1:
                print "########################### ERROR: Malformed Client Data ###########################"
                print "\nThe variable named <", key, "> contains periods, which are not allowed"
                print "\n####################################################################################"
                raise ValueError

            # Create attribute based on the type in the json data
            ty = val['type']
            if ty == 'float':
                setattr(self.data, key, float(val['value']) * self.__conversion__)
            elif ty == 'string':
                setattr(self.data, key, val['value'])
            elif ty == 'int':
                setattr(self.data, key, int(val['value']))
            else:
                raise ValueError('Unknown type ' + ty + 'in client data')
        return

    #
    # Database read routine
    #
    def __readDb__(self, recordnum):
        self.info={}

        # open the client file and read data
        SDB = Sewdb()
        SDB.open()

        query = """SELECT * FROM measurements02 WHERE id='%s';""" % recordnum

        SDB.doquery(query)
        result = SDB.store_result()
        data = result.fetch_row(how=1)
        if len(data) == 0:
            print "Unable to fetch client data from DataBase"
            raise
        cdata = data[0]

        # Check to make sure we have units
        try:
            units = cdata['units']
            if units == 'cm':
                #self.__conversion__ = cm_to_pt
                self.__conversion__ = CM_TO_PX
            elif  units == 'in':
                #self.__conversion__ = in_to_pt
                self.__conversion__ = IN_TO_PX
        except KeyError:
            print 'Client Data measurement units not defined in client data'
            raise

        # read everything into attributes
        for key, val in cdata.items():
            if len(key.split('.')) > 1:
                print "########################### ERROR: Malformed Client Data ###########################"
                print "\nThe variable named <", key, "> contains periods, which are not allowed"
                print "\n####################################################################################"
                raise ValueError

            if key == 'customername':
                setattr(self.data, key, val)
            elif key == 'units':
                setattr(self.data, key, val)
            elif key == 'id':
                setattr(self.data, "database_id", val)
            else:
                # it's a float
                setattr(self.data, key, float(val) * self.__conversion__)
        return

    def __dump__(self, obj, parent = '', parentstring = '', outtxt = []):
        objAttrs = dir(obj)

        # walk through the attributes in this object
        for oname in objAttrs:

            # we don't care about internal python stuff
            if oname.startswith('__'):
                continue

            # get the actual object we're looking at
            thisobj = getattr(obj, oname)

            # is it one of our own clientdata objects?
            if isinstance(thisobj, ClientData):
                # if so, then call dump on it
                if parentstring != '':
                    dot = '.'
                else:
                    dot = ''
                self.__dump__(thisobj, oname, (parentstring + dot + oname), outtxt)
            else:
                # if not, then it is an 'end item' bit of information
                # TODO convert back to the units used for input (not pts)
                if parent != '':
                    outtxt.append(parentstring + "." + oname + " " + str(thisobj) + "\n")
                else:
                    outtxt.append(oname + " " + str(thisobj) + "\n")
        return(outtxt)

    def dump(self):
        ot = ''
        output = sorted(self.__dump__(self.data))
        for line in output:
            ot = ot + line
        return ot

