#!/bin/bash

if [ $# != 1 ]; then
    echo "Usage: bash 14.sh <num :: int>"
    exit 1
fi

head --line=$1 hightemp.txt
