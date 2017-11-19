#!/bin/bash


if [ $# -eq 0  ]
then
	RPATH='/etc/resolv.conf'
else
	RPATH=$1
fi

DATA=`cat $RPATH`
DNS=`echo "$DATA" | sed -n '/^nameserver */p' | wc -l`

echo "you have $DNS dns server(-s) in file $RPATH"
