#NOT CURRENTLY USED
#intended to create text version and csv with note column versions of queries to read into NimbleMiner

import pandas as pd
import os

#get most recent ouput from snscraper
filename = 'out'
i=1
while os.path.isfile(filename + '.csv'): #dynamically create filename to prevent duplicates, as they do not overwrite
    if filename == 'out':
        filename = 'out2'
    else:
        i +=1
        filename = 'out' + str(i)
        
if i-1 == 0: filename = 'out.csv'
else: filename = 'out' + str(i-1) + '.csv'
   

#output as txt file
file = pd.read_csv(filename)
newName = ''
for i in range(0,len(filename)-4):
    newName+=filename[i]
newName += '.txt'
file.to_csv(newName, sep=' ', index=False, header=False)

#output as original csv, but with added Note column
file['Note'] = ''
newName = ''
for i in range(0,len(filename)-4):
    newName+=filename[i]
newName += 'n.csv'
file.to_csv(newName,index=False)