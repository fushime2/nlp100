#!/bin/bash

if [ $# != 1 ]; then
    echo "Usage: bash 16.sh <num(per file) :: int>"
    exit 1
fi

split -l $1 hightemp.txt
