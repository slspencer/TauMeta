#!/bin/bash
# tmtp.sh
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

# change the following two lines to match your installation
cd /home/susan/src/tmtp-private/standalone

TMTP_BASE=/home/susan/src/tmtp-private/standalone/
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
    #FILE="$CUSTOMER_DIR/$FILE-$D"
    echo $FILE

    return;
}

function Tmtp () {

    #Include this option to show additional debug messages, and run ./tmtp.sh from a terminal:   --debug=prints $FILE.svg

    # run mkpattern script to generate the pattern
    #$TMTP_BASE/mkpattern --client=$CUSTOMER_NAME --pattern=$PATTERN --styles=$TMTP_BASE/tmtp_styles.json $FILE.svg
    ./mkpattern --pattern=./patterns/$FILE.py --clientrecord=24 ./output/$FILE.svg

    #TODO: add if statement to run inkscape with reference layer visible or hidden.

    # run inkscape to outset the cutting lines and to view svg file.
    inkscape --file=./output/$FILE.svg --verb=ZoomPage --select=A.cuttingline --select=B.cuttingline --select=C.cuttingline\
    --select=D.cuttingline --select=E.cuttingline --select=F.cuttingline --select=G.cuttingline --select=H.cuttingline\
    --select=I.cuttingline --select=J.cuttingline --select=K.cuttingline --select=S.cuttingline\
    --verb=SelectionOffset --verb=EditDeselect --verb=FileSave | zenity --progress --title='Please wait, opening Inkscape...'\
    --text='* Tip: Save pattern as PDF before printing *' --auto-close

    # TODO: add menu item to print file - open inkscape without gui, save to pdf, use a linux print utility (not inkscape)
    # inkscape --file=$FILE.svg --export-area-snap -A $FILE.pdf

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
 --filename=$PATTERN_BASE --file-filter='*.py')"
    echo $PATTERN
    return;
    }

function MainMenu () {
    # Loop until user selects EXIT
    # TODO: add option to open existing pattern .svg file\
    # TODO: make this script more robust
    # TODO: either remove the Cancel & OK buttons or make them work

    var1="$(zenity --list --radiolist\
 --text '*        Welcome to Tau Meta Tau Physica                               *'\
 --column='' --column='What do you want to do?'\
 FALSE 'Create a Pattern with Reference Points'\
 FALSE 'Exit' )"

    case $var1 in
        "Create a Pattern with Reference Points")
          GETPATTERN="1";;
        *)
          GETPATTERN="0";;
    esac

    return;
    }

# Main Program

GETPATTERN="1"

while true; do

    PATTERN=""
    CUSTOMER_NAME=""
    CUSTOMER_DIR=""

    MainMenu

    if [ $GETPATTERN == '0' ]; then
        break
    else
        PatternMenu
        #CustomerMenu
        FileName
        Tmtp
    fi

done

# to use this menu with the sample pattern:
# Select generating a pattern with reference points ane grid lines, or without them.
# Choose which pattern to generate -. The tmtp/standalone/patterns directory opens by default.
#       You may navigate to another directory if you have stored your patterns there.
#       Click twice on the pattern name or click the Open button at the bottom of the dialog.
# Choose which customer file to use. The tmtp/standalone/customers directory opens by default.
#       Click on the customer's directory then click on the measurement file.
# The output file will be saved to the customer's directory. The pattern, date and time are used to create the file name.

# This menu will always generate messages that it couldn't find some id's
# because the inkscape command line calls more pattern piece id's than are in most pattern files.
