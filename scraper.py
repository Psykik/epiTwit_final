# As of 4/21/23 and the Twitter API changes that happened around that time, this code no longer works.
# However, you can still see the results of our ~17 queries we ran before that time in the 'files' folder
import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools, os
import yaml

from symptomCombine import *
#creates query from list of keywords using our functions in symptomCombine.py
symptom = read_symptoms('symptoms.csv')
keywords = to_queryList(symptom)
#keywords = ["covid", "cough", "dry AND throat", "no AND smell", "short AND breath", "feverish","difficulty AND breathing", "can't AND smell"]
query = ""
for i in keywords:
    if query == "":
        query += i
    else:
        query += " OR {}".format(i)

#serological time window
since = '2020-08-01'
until = '2021-06-01'

#centralmost coord of US (used for geolocation by radius)
loc = '39.50, 98.35, 10000km'


#pandas dataframe of tweets that match query and time window
def geoQuery(keys, loc):
    df = pd.DataFrame({'rawContent': []})
    kSize = {}
    for key in keys:
        try:
            df1 = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper('{} geocode:"{}" lang:en'.format(key,loc)).get_items(), 250))[['rawContent']] #['user','date','rawContent','place']
            kSize[key] = len(df1.index)
            df = pd.concat([df,df1])
        except:
            print(key + ' did not return tweets.')
            kSize[key] = 0
            continue
    return df, kSize

df,kSize = geoQuery(keywords,loc)
with open('count.yaml', 'w') as outfile: #count of tweets found for each 
    yaml.dump(kSize, outfile)


#print out information about dataframe
print(df.columns)
print(df)
print(df.shape[0])
#convert dataframe to csv
filename = 'out'
i=2
while os.path.isfile(filename + '.csv'): #dynamically create filename to prevent duplicates, as they do not overwrite
    print('rewrite')
    if filename == 'out':
        filename = 'out2'
    else:
        i +=1
        filename = 'out' + str(i)

#print(os.path.isfile('out.csv'))
df.to_csv(filename+'.csv',index=False)
