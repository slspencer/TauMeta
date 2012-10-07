#!/bin/bash
# tmtpzenmenu.sh
#
# This file is part of the tmtp open source project
#
# Copyright (C) 2010, 2011, 2012 Susan Spencer, Steve Conklin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. Attribution must be given in
# all derived works.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses>.
#

TMTP_BASE=$PWD
PATTERN_BASE=$TMTP_BASE/patterns/
CUSTOMER_BASE=$TMTP_BASE/customer/
PYTHONPATH=$PYTHONPATH:$TMTP_BASE:$PATTERN_BASE:$CUSTOMER_BASE
export PYTHONPATH
export TMTP_BASE
export PATTERN_BASE
export CUSTOMER_BASE

function FileName () {
    D=$(date +"%F"-%H%M)
    FILE=${PATTERN##*/}
    FILE=${FILE%%.*}
    FILE="$CUSTOMER_DIR/$FILE-$D"

    return;
}

function Tmtp () {

    #$TMTP_BASE/mkpattern --verbose  --client=$CUSTOMER_NAME --pattern=$PATTERN --styles=$TMTP_BASE/tmtp_styles.json --debug=prints $FILE.svg

    $TMTP_BASE/mkpattern --client=$CUSTOMER_NAME --pattern=$PATTERN --styles=$TMTP_BASE/tmtp_styles.json $FILE.svg
    
    inkscape --file=$FILE.svg --verb=ZoomPage --select=A.cuttingline --select=B.cuttingline --select=C.cuttingline\
    --select=D.cuttingline --select=E.cuttingline --select=F.cuttingline --select=G.cuttingline --select=S.cuttingline\
    --verb=SelectionOffset --verb=FileSave
    
    #--verb=EditDeselect 

    #inkscape --file=$FILE.svg --export-area-snap -A $FILE.pdf

    return;
    }

function CustomerMenu () {

    # Display menu and interact based on the user's input

    CUSTOMER_NAME="$(zenity  --file-selection\
 --title '*        Select A Customer:                     *'\
 --filename=$CUSTOMER_BASE\
 --file-filter='*.json')"

    CUSTOMER_DIR=${CUSTOMER_NAME%/*}

    return;
    }

function PatternMenu () {

    # Display menu and interact based on the user's input
    #Display menu and interact based on the user's input


    PATTERN="$(zenity  --file-selection\
 --title '*        Select A Pattern:                       *'\
 --filename=$PATTERN_BASE\
 --file-filter='*.py')"

    return;
    }

function MainMenu () {
    # Loop until user selects EXIT

    var1="$(zenity --list --radiolist\
 --text '*        Welcome to Tau Meta Tau Physica                               *'\
 --column='' --column='What do you want to do?'\
 FALSE 'Create a Pattern'\
 FALSE 'Exit TMTP' )"

    case $var1 in 
        "Create a Pattern")
          GETPATTERN="1";;
        *)
          GETPATTERN="0";;
    esac

    return;
    }

# Main Program

GETPATTERN="1"

while true; do

    MainMenu

    if [ $GETPATTERN == '0' ]; then
        break
    else
        PatternMenu
        CustomerMenu
        FileName
        Tmtp
    fi

done

