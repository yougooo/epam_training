#!/bin/bash


[ $# -eq 0  ] && path=$PWD || path=$1

base=${path##*/}     # for take local path in function,
abs=${path%%$base}   # 'base' it's start directory name
                     # 'abs' it's other part of absolute
		     # path without 'base'. 

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
	    [ -f $file ] && echo "File: ${file##$abs} `bincheck $file`"
	    [ -d $file ] && echo "Directory: ${file##$abs}" && tree_like $file  
	done
             }

echo "Full path is $path"
echo Directory: ${path##$abs}

temp=`tree_like $path`

echo "`python space.py "$temp"`"

exit 0

