#!/bin/bash
# tmtp.sh
#
# This file is part of the tmtp open source project
#
# Copyright (C) 2010, 2011, 2012, 2013, 201 Susan Spencer, Steve Conklin
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
    ans="$(zenity  --list  --text 'Select Measurements' --radiolist  --column '' --column 'Measurements' TRUE 'Dress Form - Large' FALSE 'Susan')"
    case $ans in
        "Dress Form - Large")
          NAME="DressFormLg";
          RECORD_NO="24";;
        "Susan")
          NAME="Susan";
          RECORD_NO="27";;
    esac
    return;
    }


# Main

    PATTERN=$1
    RECORD_NO=""
    RecordMenu
    GetFileName
    RunMkpattern    

#done

