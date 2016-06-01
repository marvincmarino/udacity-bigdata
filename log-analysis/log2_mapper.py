#!/usr/bin/python

# mapper for log analysis - pt 2
# number of hits by specific ip address 


import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, identity, user, time, zone, reqmethod, reqstring, reqprotocol, status, size = data
        print "{0}\t{1}".format(ip, 1)

