#!/usr/bin/env python
from operator import itemgetter
import sys
current_sum = 0
curr_combo=None
listtemp= [0,0,0]
listsystem=["0-0","0-0","0-0"]
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    buildsys, temp = line.split(',')
    buildid,sysid = buildsys.split('-')
    # convert count (currently a string) to int
    try:
        temp = int(temp)
        #counter=int(counter)
        #buildid=int(buildid)
        #sysid=int(sysid)
    except ValueError:
        # count was not ai number, so silently
        # ignore/discard this line
        continue
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if curr_combo== buildsys:
            current_sum += temp
            #count=count+counter+1
            
            # min1=min(listtemp)
            # minpos = listtemp.index(min1) 
            # if(current_sum)>  min1:
            #         listtemp[minpos]=current_sum
            #         listsystem[minpos]= buildsys
    else:
        if curr_combo:
            # write result to STDOUT
            min1=min(listtemp)
            minpos = listtemp.index(min1) 
            if(current_sum)>  min1:
                    listtemp[minpos]=current_sum
                    listsystem[minpos]= curr_combo
                    #print(listsystem,listtemp)
        current_sum=temp
        curr_combo=buildsys
        
# do not forget to output the last word if needed!
if curr_combo == buildsys:
            min1=min(listtemp)
            minpos = listtemp.index(min1)
            if(current_sum)>  min1:
                    listtemp[minpos]=current_sum
                    listsystem[minpos]= curr_combo
#                    print(listsystem,listtemp)

print('\nThe worst system are ')

for i in listsystem:
        data1,data2= i.split('-')
        print('\n\n The Building id is : %s ,  and System id is : %s ' % (data1,data2))
