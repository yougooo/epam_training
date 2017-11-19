#!/bin/bash

[[ $1 =~ ^[0-9][0-9]?$ ]] && FREESPACE=$1 || FREESPACE=10

used=$(echo 100-$FREESPACE | bc)
freechek=`df -h | awk '(NR!=1) && ($5 > "'"$used"'") {print}'`

[[ ! $freechek ]] && echo 'you have enough free space' || echo 'you have problems with:'; echo "$freechek"

exit 0
