#!/bin/bash

####### for loop ##########
echo 'for output' 
for i in $*
do
	echo $i
done
echo 'end for output'
echo
############################


temp=${@:1} # define variable 'temp' for next using in 
            # until loop because shift statment remove
	    # position arguments
###### while loop ##########
echo
echo 'while output'
while [ $1 ]
do
	echo "$1"
        shift	
done
echo 'end while output'
echo
############################


# update position element from temp variable
set `echo $temp` 

###### until loop ##########
echo
echo 'until output'
until [ ! $1 ]
do
	echo $1
	shift
done
echo 'end until output'
echo
############################


