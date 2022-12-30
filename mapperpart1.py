#!/usr/bin/env python
import sys
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    data = line.split(",")
    try:
        i=int(data[2])-int(data[3])   
        s=data[6]+'-'+data[4]
        print ('%s,%s' % (s, abs(i)))
    except IndexError:
        continue
    except ValueError:
        continue
    