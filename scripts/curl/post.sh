#!/bin/bash
#make sure to chmod 755 this script ralph...

ip=`../../bin/getop $1`
if [ $? -eq 0 ]
then
	curl -i -H "Content-Type: application/json" -X POST -d '{"number":5}' $ip/test/getSquare
else
	echo $?
	echo $ip
fi

