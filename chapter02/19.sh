#!/bin/bash

cut -d ' ' -f 1 hightemp.txt | sort | uniq --count | sort -r
