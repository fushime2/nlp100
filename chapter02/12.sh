#!/bin/bash

awk '{print $1}' hightemp.txt > ./col1.txt
awk '{print $2}' hightemp.txt > ./col2.txt
