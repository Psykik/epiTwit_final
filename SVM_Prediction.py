# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 00:01:11 2023

@author: joshn
"""

from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle
import numpy as np

df = pd.read_csv('files/tweets_US_labeled.csv')

df.min = df.dropna()

X = df['text']
y = df['note']

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

#iterating through indices of manually labeled tweets
for ind in df.min.index:
    if ind == 1:
        X_train = X[ind]
    else:
        X_train = np.vstack([X_train, X[ind]])

y_train = df.min['note']

# training a linear SVM classifier
from sklearn.svm import SVC
svm_model_linear = SVC(kernel = 'linear', C = 1).fit(X_train, y_train)
#this is extremely computationally expensive, needed to free up 11GB of RAM
svm_predictions = svm_model_linear.predict(X)
  
#adding predictions as variable to dataframe
df['predicted'] = svm_predictions
#exporting dataframe
df.to_csv("svm_results.csv")