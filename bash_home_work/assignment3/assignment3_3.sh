#!/bin/bash

[ $# -eq 0  ] && path=$PWD || path=$1

base=${path##*/}     # for take local path in function,
abs=${path%%$base}   # 'base' it's start directory name
                     # 'abs' it's other part of absolute
		     # path without 'base'. 

tree_like () {
	for file in $1/*
	do
	    [ -f $file ] && echo "File: ./${file##$abs} file has: `cat $file | wc -l` lines"
	    [ -d $file ] && echo "Directory: ./${file##$abs}" && tree_like $file  
	done
}

echo "Full path is $path"
echo Directory: ./${path##$abs}

temp=`tree_like $path`

echo "`python space.py "$temp"`"

exit 0

