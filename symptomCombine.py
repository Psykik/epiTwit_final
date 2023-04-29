import pandas as pd
import math 

def read_symptoms(input): #function to read out all symptoms from symptoms.csv (originally in NimbleMiner format) into a list
    df = pd.read_csv(input)
    col = df.columns
    df =df.values.tolist()
    symptoms = []
    for i in df:
        for j in i:
            try: #cannot use .isnan() on a string, so we try and catch
                if math.isnan(j) == False: #checks if we're trying to copy a null entry from the dataset
                    symptoms.append(j) #likely don't even need this
            except: #if we couldn't use .isnan(), this is a string and we're fine
                symptoms.append(j)
    for i in col:
        symptoms.append(i)
    return symptoms

def to_queryList(symp): #turns list of symptoms into queriable set of keyphrases
    qList = [] #list of symptoms in query format (replacing spaces with ANDs)
    for phrase in symp:
        newStr = ''
        for letter in phrase:
            if letter == ' ': #if there's a space (we move to a new word in phrase), we place 'AND' in between words for the twitter query
                newStr += ' AND '
            elif letter == 'f' and len(newStr) >1: #get rid of 'of' since it's unnecessary for query
                if newStr[-1] == 'o':
                    newStr = newStr.replace(' AND o', '')
            else:
                newStr += letter
        qList.append(newStr)
    return(qList)

def to_query(qList): #take list of query-formatted symptoms
    query = ""
    for i in qList:
        if query == "":
            query += i
        else:
            query += " OR {}".format(i)
    return query