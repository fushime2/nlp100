#!/bin/bash

awk '{print $1}' hightemp.txt | sort -u
