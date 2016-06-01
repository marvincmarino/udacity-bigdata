#!/usr/bin/python

# log analysis - pt 1
# number of hits for each different file on the website

import sys

hitsTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisHit = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", hitsTotal
        oldKey = thisKey;
        hitsTotal = 0

    oldKey = thisKey
    hitsTotal += float(thisHit)

if oldKey != None:
    print oldKey, "\t", hitsTotal

