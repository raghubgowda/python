#!/usr/bin/env python
# coding: utf-8

# In[88]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib

music_data = pd.read_csv('music.csv')
X = music_data.drop(columns=['genre'])
y = music_data['genre']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
joblib.dump(model, 'music_recommender.joblib')
predictions = model.predict(X_test)

score = accuracy_score(y_test, predictions)
score


# In[91]:


from sklearn.externals import joblib

model = joblib.load('music_recommender.joblib')
predictions = model.predict([[21, 1]])
predictions


# In[93]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

music_data = pd.read_csv('music.csv')
X = music_data.drop(columns=['genre'])
y = music_data['genre']

model = DecisionTreeClassifier()
model.fit(X, y)

tree.export_graphviz(model, out_file='music-recommender.dot', 
                     feature_names=['age', 'gender'],
                     class_names=sorted(y.unique()),
                     label='all',
                     filled=True,
                     rounded=True)

