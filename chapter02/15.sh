#!/bin/bash

if [ $# != 1 ]; then
    echo "Usage: bash 15.sh <num :: int>"
    exit 1
fi

tail -n $1 hightemp.txt
