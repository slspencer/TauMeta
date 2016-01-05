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
PRINTER1='SC-T7000-Series-4'

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
    ans="$(zenity --list --radiolist --title 'Tau Meta Tau Physica' --text='Print Pattern?'  --column ' ' --column 'Print ' FALSE 'Print to SC-T7000 Plotter' TRUE 'Do not Print')"
    
    case $ans in
        "Print to SC-T7000 Plotter")
          PRINTPATTERN="1";;
        *)
          PRINTPATTERN="0";;
    esac
        
    if [ $PRINTPATTERN == '1' ]; then 

        #convert SVG to PDF with Inkscape no gui (--z) export to PDF (-A)
           
        inkscape --without-gui --file=$SVG --export-area-snap -A $PDF | zenity --info --title="Convert pattern" --text="* Converting $SVG to PDF *" 
        wait   

        #send file to hardcoded print queue $PRINTER1!!!!         
        lpr -P $PRINTER1 $PDF | zenity --info --title="Print pattern" --text="* Sending $PDF to $PRINTER1 *"
        (exec system-config-printer --show-jobs SC-T7000-Series-4)
   
    fi    
    
    return;

    }

function MakePattern () {
    #set the client to database or .json file
    
    if [ $MEASUREMENTSOURCE == 'Database' ]; then 
        CLIENT="--clientrecord=$RECORD_NO"
    elif [ $MEASUREMENTSOURCE == 'JSON' ]; then
        CLIENT="--client=$CUSTOMER_BASE/$CUSTOMER_DIR/$CUSTOMER_FILE"
    fi

    STYLES="--styles=tmtp_styles.json"   
    PATTERN="--pattern=$PATTERN_BASE/$FILE.py"
    SVG="$CUSTOMER_BASE/$CUSTOMER_DIR/$OUTPUT_FILE.svg"
    PDF="$CUSTOMER_BASE/$CUSTOMER_DIR/$OUTPUT_FILE.pdf"

    #Include this option to show additional debug messages: --debug=prints
    # @@@ MAKE THE PATTERN WITH MKPATTERN @@@
    echo 'PATTERN='$PATTERN
    echo 'CLIENT='$CLIENT
    echo 'SVG='$SVG
    $TMTP_BASE/mkpattern $PATTERN $CLIENT $SVG

    #TODO: add if statement to run inkscape with reference layer visible or hidden.

    # run inkscape to outset the cutting lines and to view svg file.
    inkscape --file=$SVG \
    --select=A.cuttingline --select=B.cuttingline --select=C.cuttingline \
    --select=D.cuttingline --select=E.cuttingline --select=F.cuttingline \
    --select=G.cuttingline --select=H.cuttingline --select=I.cuttingline \
    --select=J.cuttingline --select=K.cuttingline --select=L.cuttingline \
    --verb=SelectionOffset --verb=EditDeselect --verb=FileSave \
    --verb=ZoomPage | zenity --progress \
    --title='Please wait, opening Inkscape...'\
    --text="* Creating $CUSTOMER_DIR/$CUSTOMER_FILE *" --auto-close
    
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

function GetDatabaseMeasurements () {
    CUSTOMER_NAME="$(zenity --list --radiolist --title 'Tau Meta Tau Physica' --text='Select Measurements' --column ' ' --column 'Measurements' TRUE 'DressFormLg' FALSE 'Susan' )"
    
    case $CUSTOMER_NAME in
        "DressFormLg")
          CUSTOMER_DIR="DressFormLg";
          RECORD_NO="24";;
        "Susan")
          CUSTOMER_DIR="Susan";
          RECORD_NO="27";;
    esac
     
    return;
    }

function GetJSONMeasurements () {
    # Display menu and interact based on the user's input
    CUSTOMER_FULL_FILE_PATH="$(zenity  --file-selection --title '*        Select A Customer:                     *' --filename=$CUSTOMER_BASE/ --file-filter='*.json')"
    echo "CUSTOMER_FULL_FILE_PATH=$CUSTOMER_FULL_FILE_PATH"
    
    #file name
    CUSTOMER_FILE=$(basename $CUSTOMER_FULL_FILE_PATH)
    echo "CUSTOMER_FILE=$CUSTOMER_FILE"  
       
    #full path minus file name
    CUSTOMER_PATH=$(dirname $CUSTOMER_FULL_FILE_PATH)
    echo "CUSTOMER_PATH=$CUSTOMER_PATH"
    
    #last directory in path
    CUSTOMER_DIR=$(basename $CUSTOMER_PATH)
    echo "CUSTOMER_DIR=$CUSTOMER_DIR" 
     
    #file name minus extension
    CUSTOMER_NAME=${CUSTOMER_FILE%.*}
    echo "CUSTOMER_NAME=$CUSTOMER_NAME"
    
    return;
    }

function GetMeasurements () {
    MEASUREMENTSOURCE="$(zenity --list --radiolist --title 'Tau Meta Tau Physica' --text='Select Measurement Source' --column ' ' --column 'Source' TRUE 'JSON' FALSE 'Database' )"
    
    case $MEASUREMENTSOURCE in
        "JSON")
          GetJSONMeasurements;;
        "Database")
          GetDatabaseMeasurements;;
    esac
    
    return;
    }

function GetPattern () {
    PATTERN="$(zenity  --file-selection --title 'Tau Meta Tau Physica - Select Pattern' --filename=$PATTERN_BASE/ --file-filter='*.py' )"
    return;
    }

function MainMenu () {
    var1="$(zenity --list --radiolist \
    --title 'Tau Meta Tau Physica' \
    --text='Main Menu' \
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
