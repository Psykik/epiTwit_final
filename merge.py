import pandas as pd

#read in every dataset we collected before API restrictions
df1 = pd.read_csv('files/out.csv')
df2 = pd.read_csv('files/out2.csv')
df3 = pd.read_csv('files/out3.csv')
df4 = pd.read_csv('files/out4.csv')
df5 = pd.read_csv('files/out5.csv')
df6 = pd.read_csv('files/out6.csv')
df7 = pd.read_csv('files/out7.csv')
df8 = pd.read_csv('files/out8.csv')
df9 = pd.read_csv('files/out9.csv')
df10 = pd.read_csv('files/out10.csv')
df11 = pd.read_csv('files/out11.csv')
df12 = pd.read_csv('files/out12.csv')
df13 = pd.read_csv('files/out13.csv')
df14 = pd.read_csv('files/out14.csv')
df15 = pd.read_csv('files/out15.csv')
df16 = pd.read_csv('files/out16.csv')
df17 = pd.read_csv('files/out17.csv')

listOfdf = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df17] #makes it easier to refer to them as a whole before merge

dfMerge = pd.concat(listOfdf)
dfMerge = dfMerge.drop(['user','date','place','Note'],axis=1) #get rid of extra columns, as they aren't present in every dataset
dfMerge = dfMerge.drop_duplicates() #drop duplicates, as many datasets were based off the same, or similar, queries

#info about merged dataset to check if everything looks good
print(dfMerge.columns)
print(dfMerge.info())

#save new merged dataset as a csv
dfMerge.to_csv('Files/merged.csv',index=False)

dfMerge['Note'] = ''
dfMerge.to_csv('Files/mergedN.csv', index=False)

#---------------------------------
#Now lets do the same, but this time only for datasets with a timestamp (for potential regression)
#NOTE: This ended up being useless because we had few with a stored date
dateDFs = [] #we'll store dfs with a 'date' column here
for df in listOfdf:
    if 'date' in df.columns:
        dateDFs.append(df)

#now repeat the combining steps as before
dfDates = pd.concat(dateDFs)
dfDates = dfDates.drop(['user','place'],axis=1) #get rid of extra columns, as they aren't present in every dataset
dfDates = dfDates.drop_duplicates() #drop duplicates, as many datasets were based off the same, or similar, queries

dfDates.to_csv('Files/dateset.csv',index=False)