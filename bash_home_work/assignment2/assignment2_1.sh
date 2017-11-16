#!/bin/bash

echo "Enter your salary: "
read salary 

if [[ $salary =~ ^[0-9]+$  ]]
then
	echo
else
	echo 'Salary must be integer number!'
	exit 0
fi

tax () {
    if [[ $1 -lt 5000  ]]
    then
	   echo 'your tax is 0'
    elif [[ $1 -ge 5000 && $1 -lt 30000  ]]
    then
	   echo 'your tax is 10%'
    else
	   echo 'your tax is 20%'
    fi

}

tax $salary

exit 0 
