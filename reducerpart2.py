#!/usr/bin/env python
from operator import itemgetter
import sys
current_sum = 0
curr_combo=None
listtemp= [0,0,0]
listsystem=["","",""]
dictdays = {x: 0 for x in range(9, 18)}
nodictdays = {x: 0 for x in range(9, 18)}
diclist=[{},{},{}]
nodiclist=[{},{},{}]
avglist=[{},{},{}]
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    buildid, hour,temp,inputlist= line.split('-')
    
    # convert count (currently a string) to int
    try:
        inputlist=eval(inputlist)
        temp = int(temp)
        #counter=int(counter)
        
        hour=int(hour)
        
    except ValueError:
        # count was not ai number, so silently
        # ignore/discard this line
        print("error")
        continue
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if curr_combo== buildid:
            current_sum = current_sum + temp
            if hour in dictdays:
                dictdays[hour]=dictdays[hour]+temp
                nodictdays[hour]=nodictdays[hour]+1         
    else:
        if curr_combo:
            # write result to STDOUT
             min1=min(listtemp)
             minpos = listtemp.index(min1) 
             if(current_sum)>  min1:
                     listtemp[minpos]=current_sum
                     listsystem[minpos]= curr_combo
                     diclist[minpos]=dictdays
                     nodiclist[minpos]=nodictdays
                     
                     for i in range (9,18):
                        try:
                                        avglist[minpos][i] = float (dictdays[i])/float(nodictdays[i])
                        except:
                            avglist[minpos][i]=0
                     #print(listtemp,listsystem, diclist,nodiclist,avglist)#,dictdays)
        current_sum=temp

        curr_combo=buildid

        dictdays=inputlist

        
        nodictdays = {x: 0 for x in range(9, 18)}
    

# do not forget to output the last word if needed!
if curr_combo == buildid:
            min1=min(listtemp)
            minpos = listtemp.index(min1)
            if(current_sum)>  min1:
                     listtemp[minpos]=current_sum
                     listsystem[minpos]= curr_combo
                     diclist[minpos]=dictdays
                     nodiclist[minpos]=nodictdays
                     
                     for i in range (9,18):
                        try:
                                        avglist[minpos][i] = float (dictdays[i])/float(nodictdays[i])
                        except:
                            avglist[minpos][i]=0



print('\n\nThe building id for 3 hottest buildings (business hours 9:00 to 17:00)  are : ', listsystem)
for i in range(3):
            print("\nBuiding id:  %s  , average temperature for each hour %s" % (listsystem[i],avglist[i] ))