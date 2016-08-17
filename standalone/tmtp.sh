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

TMTP_BASE=$PWD
PATTERN_BASE=$TMTP_BASE/patterns
CUSTOMER_BASE=$TMTP_BASE/customer
OUTPUT_BASE=$TMTP_BASE/output
PYTHONPATH=$PYTHONPATH:$TMTP_BASE:$PATTERN_BASE:$CUSTOMER_BASE

export TMTP_BASE
export PATTERN_BASE
export CUSTOMER_BASE
export OUTPUT_BASE
export PYTHONPATH
export CUSTOMER_FILE
export CUSTOMER_DIR
export CUSTOMER_NAME
export PATTERN
export OUTPUT

function PrintPattern () {

    (exec lpstat -v | awk '{print $3}') > PRINTER_LIST
    lines=()
    while read -r line || [[ -n $line ]]; do
        #echo "${line%?}"
        lines=("${lines[@]}" "FALSE" "${line%?}")
    done < PRINTER_LIST
    lines=("${lines[@]}" "TRUE" "Do not print")
    myprinter="$(zenity --list --radiolist --title="Tau Meta Tau Physica" --text="Select a Printer" \
    --width=800 --height=500 --column=Select --column=Printer "${lines[@]}")"
    
    if [ $myprinter != 'Do not print' ]; then 
        #convert SVG to PDF with Inkscape no gui (--z) export to PDF (-A)          
        inkscape --without-gui --file=$SVG --export-area-snap -A $PDF | \
        zenity --progress --title="Please wait, converting SVG to PDF..." --text="* Converting $SVG to PDF *" --auto-close
        wait   
        #send file to hardcoded print queue $PRINTER1 or $PRINTER2!!!!         
        lpr -P $myprinter $PDF | \
        zenity --progress --title="Please wait, printing pattern..." --text="* Sending $PDF to $myprinter *" --auto-close
        wait
        (exec system-config-printer --show-jobs $myprinter) 
    fi       
    return;
    
    }

function MakePattern () {

    STYLES="--styles=$TMTP_BASE/tmtp_styles.json"  
    PATTERN="--pattern=$PATTERN_BASE/$FILE.py"
    SVG="$CUSTOMER_BASE/$CUSTOMER_DIR/$OUTPUT_FILE.svg"
    PDF="$CUSTOMER_BASE/$CUSTOMER_DIR/$OUTPUT_FILE.pdf"
    CLIENT="--client=$CUSTOMER_BASE/$CUSTOMER_DIR/$CUSTOMER_FILE"   
    echo 'PATTERN='$PATTERN
    echo 'CLIENT='$CLIENT
    echo 'SVG='$SVG
    
    # @@@ GENERATE THE PATTERN WITH MKPATTERN @@@
    #Include this option to show additional debug messages: --debug=prints
    $TMTP_BASE/mkpattern $PATTERN $STYLES $CLIENT $SVG

    # run inkscape to outset the cutting lines and view svg file
    #TODO: add if statement to run inkscape with reference layer visible or hidden.
    # can't offset more pieces than A through L because Inkscape will crash.
    inkscape --file=$SVG \
    --select=A.cuttingline --select=B.cuttingline --select=C.cuttingline \
    --select=D.cuttingline --select=E.cuttingline --select=F.cuttingline \
    --select=G.cuttingline --select=H.cuttingline --select=I.cuttingline \
    --select=J.cuttingline --select=K.cuttingline --select=L.cuttingline \
    --verb=SelectionOffset --verb=EditDeselect --verb=FileSave \
    --verb=ZoomPage | zenity --progress \
    --title='Please wait, opening Inkscape...'\
    --text="* Creating $CUSTOMER_DIR/$OUTPUT_FILE.svg *" --auto-close
    
    return;
    }

function GetFileName () {
    D=$(date +"%F"-%H%M)
    FILE=${PATTERN##*/}
    FILE=${FILE%%.*}
    #FILE="$CUSTOMER_DIR/$FILE-$D"
    OUTPUT_FILE=$CUSTOMER_NAME-$FILE-$D
    return;
}

function GetMeasurements () {
    
    # Display menu and interact based on the user's input
    CUSTOMER_FULL_FILE_PATH="$(zenity  --file-selection \
    --title 'Tau Meta Tau Physica'  \    
    --text 'Select a Customer measurement file' \
    --width=800 --height=500 \
    --filename=$CUSTOMER_BASE/ \
    --file-filter='*.json')"
    #echo "CUSTOMER_FULL_FILE_PATH=$CUSTOMER_FULL_FILE_PATH"
    
    #file name
    CUSTOMER_FILE=$(basename $CUSTOMER_FULL_FILE_PATH)
    #echo "CUSTOMER_FILE=$CUSTOMER_FILE"  
       
    #full path minus file name
    CUSTOMER_PATH=$(dirname $CUSTOMER_FULL_FILE_PATH)
    #echo "CUSTOMER_PATH=$CUSTOMER_PATH"
    
    #last directory in path
    CUSTOMER_DIR=$(basename $CUSTOMER_PATH)
    #echo "CUSTOMER_DIR=$CUSTOMER_DIR" 
     
    #file name minus extension
    CUSTOMER_NAME=${CUSTOMER_FILE%.*}
    #echo "CUSTOMER_NAME=$CUSTOMER_NAME"
    
    return;
    }


function GetPattern () {
    PATTERN="$(zenity  --file-selection \
    --title 'Tau Meta Tau Physica'  \
    --text 'Select a Pattern file' \
    --width=800 --height=500 --filename=$PATTERN_BASE/ \
    --file-filter='*.py' )"
    return;
    }

function MainMenu () {
    var1="$(zenity --list --radiolist \
    --title 'Tau Meta Tau Physica' \
    --text='Main Menu' --width=800 --height=500 \
    --column ' ' --column 'Main ' \
    TRUE 'Create a Pattern' \
    FALSE 'Exit' )"
    
    case $var1 in
        "Create a Pattern")
          CREATEPATTERN="1";;
        *)
          CREATEPATTERN="0";;
    esac
   
    return;
    }

#-------------
# Main

while true; do

    PATTERN=""
    RECORD_NO=""
    CUSTOMER_NAME=""
    CUSTOMER_DIR=""
    MEASUREMENT_SOURCE=""
    CLIENT=""
    CREATEPATTERN="1"

    MainMenu
    if [ $CREATEPATTERN == '0' ]; then
        break;
    else        
       GetPattern
       GetMeasurements
       GetFileName
       MakePattern
       PrintPattern      
    fi
    
done

# Choose a pattern file -. The tmtp/standalone/patterns directory opens by default.
#       You may navigate to another directory if you have stored your patterns there.
# Choose a customer measurement file. The tmtp/standalone/customers directory opens by default.
#       Choose a customer's directory then click on the measurement file.
# The output file will be saved to the customer's directory. The pattern, date and time are used to create the file name.

# Inkscape will generate messages that it couldn't find some id's
# because more pattern piece id's (A through L) are called for offsets than are in most pattern files.
