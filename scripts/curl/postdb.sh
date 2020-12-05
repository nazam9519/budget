#!/bin/bash
#make sure to chmod 755 this script ralph...

curl -i -H "Content-Type: application/json" -X POST -d '{"username":"n12","password":"123"}' localhost:5000/testauth
