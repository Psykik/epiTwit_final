from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

df = pd.read_csv('files/tweets_US_labeled.csv')

df.min = df.dropna()

X = df.min['text'].reset_index(drop = True)
y = df.min['note'].reset_index(drop = True)

#necessary resource downloads, put into console:
#import nltk
#nltk.download('wordnet')
#nltk.download('omw-1.4')

#pre-processing using script in nlpCore.py
from nlpCore import *
documents = preprocess(X)

from sklearn import feature_extraction
count_vectorizer = feature_extraction.text.CountVectorizer()
X = count_vectorizer.fit_transform(documents).toarray()

#variables to hold accuracy, sensitivity, and specificity for each iteration of loop below

acc = []
sen = []
spe = []

#loop to repeat classification and ML for a number of times
i = 0
while i < 100:
    # dividing X, y into train and test data, 75%-25% split
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = i)

    # training a linear SVM classifier
    from sklearn.svm import SVC
    svm_model_linear = SVC(kernel = 'linear', C = 1).fit(X_train, y_train)
    svm_predictions = svm_model_linear.predict(X_test)
  
    # model accuracy for X_test  
    accuracy = svm_model_linear.score(X_test, y_test)
  
    # creating a confusion matrix
    cm = confusion_matrix(y_test, svm_predictions)

    #calculating sensitivity from confusion matrix
    sensitivity = cm[0][0] / (cm[0][0] + cm[0][1])
    #calculating specificity from confusion matrix
    specificity = cm[1][1] / (cm[1][1] + cm[1][0])
    
    acc.append(accuracy)
    sen.append(sensitivity)
    spe.append(specificity)
    
    i += 1
    
    if i%5 == 0:
        print("{}% Complete".format(i))
    
#Printing outputs (avg of list data)
print()
print("Average Classifier Accuracy: {}\n".format(sum(acc)/100))
print("Average Classifier Sensitivity: {}\n".format(sum(sen)/100))
print("Average Classifier Specificity: {}\n".format(sum(spe)/100))

