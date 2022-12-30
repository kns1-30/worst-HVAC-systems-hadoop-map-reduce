#!/usr/bin/env python
import sys
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    data = line.split(",")
    try:
        time=data[1]
        i=int(data[3])
        s=data[6]
        hourlist = time.split(':')
        hour=hourlist[0]
        hour=int(hour)
        if(hour in range(9,18)):
            dictdays = {x: 0 for x in range(9, 18)}
            dictdays[hour]=i
            print ('%s-%s-%s-%s' % (s,hour, i,dictdays))
    except IndexError:
        continue
    except ValueError:
        continue