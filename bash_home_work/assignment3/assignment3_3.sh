#!/bin/bash


[ $# -eq 0  ] && path=$PWD || path=$1
[ -f $path  ] && echo 'File detected!' && exit 65


bincheck () {
	if [[ -s $1 ]]                
	then
		if [[ `file --mime-encoding $1 | awk '($2=="binary") {print $2}'` ]]
		then
			echo 'is binary'
		else
			echo "has: `cat $1 | wc -l` lines"
		fi	
        else
		echo 'has: 0 lines'
	fi 
            }



tree_like () {
	for file in $1/*
	do
	    [ -f $file ] && echo "File: $file `bincheck $file`"
	    [ -d $file ] && echo "Directory: $file" && tree_like $file  
	done
             }


echo "Full path is $path"
echo Directory: `basename $path`
temp=`tree_like $path`
echo "`python space.py "$temp"`"

exit 0

