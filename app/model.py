import os
import pickle
import numpy as np
import collections
import re
import gensim

from gensim.models.doc2vec import Doc2Vec, TaggedDocument                      
from sklearn.linear_model import LogisticRegression                            
   

#Load DBOW model                                                                                                                             
dbow = Doc2Vec.load("models/dbow_paragraph.model")
filename = 'models/Logistic_topic_clasifier_from_paragraph.sav'
#Load Logistic Regression model                                                                                                              
logreg = pickle.load(open(filename, 'rb'))
#Write a dictionary of classes                                                                                                               
class_tokens=zip(range(48),logreg.classes_)
classDecoder=dict(class_tokens)
dictionary_filepath="classes_dictionary/section_names_dict.pkl"
classes_dictionary = pickle.load(open(dictionary_filepath, 'rb'))

