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

TMTP_BASE=/home/susan/src/tmtp-private/standalone
PATTERN_BASE=$TMTP_BASE/patterns
CUSTOMER_BASE=$TMTP_BASE/customer
OUTPUT_BASE=$TMTP_BASE/output
PYTHONPATH=$PYTHONPATH:$TMTP_BASE:$PATTERN_BASE:$CUSTOMER_BASE

export PYTHONPATH
export TMTP_BASE
export PATTERN_BASE
export CUSTOMER_BASE

function PrintPatternMenu () {
    ans="$(zenity  --list  --text 'Print This Pattern?' --radiolist  --column '' --column 'Choice' FALSE 'Yes, Print this Pattern' TRUE 'No, do not Print this Pattern')"
    
    case $ans in
        "Yes, Print this Pattern")
          PRINTPATTERN="1";;
        *)
          PRINTPATTERN="0";;
    esac
    
    echo PRINTPATTERN = $PRINTPATTERN

    if [ PRINTPATTERN == '1' ]; then 
        #run inkscape no gui (--z)  export to pdf (-A) 
        
        inkscape --without-gui --file=$OUTPUT_BASE/$NAME/$OUTPUT_FILE.svg --export-area-snap \
         -A $OUTPUT_BASE/$NAME/$OUTPUT_FILE.pdf \
         | zenity --progress --title='Please wait, printing pattern...' \
         --text='* Tip: Check ink prior to printing *' --auto-close
         
        $OUTPUT_BASE/$NAME/$OUTPUT_FILE.pdf | lpr -P SC-T7000-Series
        wait
        wait
        wait    
    fi
    
    }

function RunMkpattern () {

    #Include this option to show additional debug messages, and run ./tmtp.sh from a terminal:   --debug=prints $FILE.svg

    # run mkpattern script to generate the pattern
    #$TMTP_BASE/mkpattern --client=$CUSTOMER_NAME --pattern=$PATTERN --styles=$TMTP_BASE/tmtp_styles.json $FILE.svg
    #./mkpattern --pattern=./patterns/$FILE.py --clientrecord=24 ./output/$FILE.svg
    $TMTP_BASE/mkpattern --pattern=$PATTERN_BASE/$FILE.py --clientrecord=$RECORD_NO $OUTPUT_BASE/$NAME/$OUTPUT_FILE.svg

    #TODO: add if statement to run inkscape with reference layer visible or hidden.

    # run inkscape to outset the cutting lines and to view svg file.
    inkscape --file=$OUTPUT_BASE/$NAME/$OUTPUT_FILE.svg --verb=ZoomPage \
    --select=A.cuttingline --select=B.cuttingline --select=C.cuttingline \
    --select=D.cuttingline --select=E.cuttingline --select=F.cuttingline \
    --select=G.cuttingline --select=H.cuttingline --select=I.cuttingline \
    --select=J.cuttingline --select=K.cuttingline --select=S.cuttingline \
    --verb=SelectionOffset --verb=EditDeselect --verb=FileSave | zenity --progress \
    --title='Please wait, opening Inkscape...'\
    --text='* Tip: Save pattern as PDF before printing *' --auto-close
    
    wait
    wait
    wait
    PrintPatternMenu

    return;
    }

function GetFileName () {
    D=$(date +"%F"-%H%M)
    FILE=${PATTERN##*/}
    FILE=${FILE%%.*}
    #FILE="$CUSTOMER_DIR/$FILE-$D"
    echo $FILE
    OUTPUT_FILE=$NAME-$FILE-$D
    echo $OUTPUT_FILE

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

function RecordMenu () {
    ans="$(zenity  --list  --text 'Select Measurements' --radiolist  --column '' --column 'Measurements' FALSE 'DressFormLg' TRUE 'Susan')"
    case $ans in
        "DressFormLg")
          NAME="DressFormLg";
          RECORD_NO="27";;
        "Susan")
          NAME="Susan";
          RECORD_NO="24";;
    esac
    return;
    }


function PatternMenu () {

    # Display menu and interact based on the user's input
    #Display menu and interact based on the user's input
    PATTERN="$(zenity  --file-selection\
 --title '*        Select A Pattern:                       *'\
 --filename=$PATTERN_BASE/ --file-filter='*.py')"
    echo $PATTERN
    return;
    }

function CreateMenu () {
    var1="$(zenity --list --radiolist\
 --text '*        Welcome to Tau Meta Tau Physica                               *'\
 --column='' --column='What do you want to do?'\
 FALSE 'Create a Pattern with Reference Points'\
 FALSE 'Exit' )"
    case $var1 in
        "Create a Pattern with Reference Points")
          CREATEPATTERN="1";;
        *)
          CREATEPATTERN="0";;
    esac
    return;
    }

#-------------
# Main

GETPATTERN="1"

while true; do

    PATTERN=""
    RECORD_NO=""
    CUSTOMER_NAME=""
    CUSTOMER_DIR=""

    CreateMenu
    if [ $CREATEPATTERN == '1' ]; then
        PatternMenu
        #CustomerMenu
        RecordMenu
        GetFileName
        RunMkpattern
    else
        break
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
