#!/usr/bin/python


import numpy as np
import pylab as pl

from sklearn.naive_bayes import GaussianNB


X = np.array([[1,2], [-2,2], [4,5]]) #features
Y = np.array([1, 1, 2]) #labels

clf = GaussianNB()  #create classifier 
clf.fit(X, Y) #give training data to set patterns
GaussianNB()
print(clf.predict([[5,5]])) #predict for new point
