#!/bin/sh

EXPECTED_ARGS=3
E_BADARGS=65

if [ $# -ne $EXPECTED_ARGS ]
then
  echo "Usage: `basename $0` dir/ oldtext newtext"
  exit $E_BADARGS
fi

grep -rl $2 $1 |
 while read filename
 do
 (
  echo $filename
  sed -i "s/$2/$3/g;" $filename
 )
 done
