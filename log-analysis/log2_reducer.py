#!/usr/bin/python

# log analysis - pt2
# number of her of hist from a specific ip

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

