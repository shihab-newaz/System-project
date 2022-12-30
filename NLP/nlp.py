import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import nltk
import re
from nltk.corpus import stopwords
dataframe = pd.read_csv("EcoPreprocessedv2.csv")
dataframe.rename(columns={'division':'target'}, inplace=True)
dataframe.reset_index(drop=True,inplace=True)
y = dataframe['target'].replace({'positive':1, 'neutral':0, 'negative':-1})
X = dataframe['review']


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.feature_extraction.text import HashingVectorizer
vectorizer = HashingVectorizer(n_features=2**20) 
X_train=vectorizer.fit_transform(X_train)
X_test=vectorizer.transform(X_test)
  
from sklearn.svm import SVC
svc_lin = SVC(kernel='linear', random_state=0)
svc_lin.fit(X_train, y_train)
    
from sklearn.metrics import accuracy_score
y_pred = svc_lin.predict(X_test)
l=accuracy_score(y_test, y_pred)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test, y_pred)
#print('Accuracy:' ,l*100,"%")

review =['simple and convenient']
review = vectorizer.fit_transform(review)
predict = svc_lin.predict(review)
#print(predict)
    
import pickle
pickle.dump(svc_lin,open("model.sav", "wb"))
pickle.dump(vectorizer, open("hashvectorizer.sav", "wb"))    