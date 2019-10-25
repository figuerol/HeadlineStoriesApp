from flask import Flask
from flask_bootstrap import Bootstrap
from flask import request, render_template, flash, redirect, url_for
from flask_bootstrap import __version__ as FLASK_BOOTSTRAP_VERSION
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from markupsafe import escape
#from model import dbow, logreg, classDecoder, classes_dictionary
import numpy as np
import gensim
from gensim.summarization import keywords

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



#frontend = Blueprint('frontend', __name__)

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def main():
    
    return redirect('/index')


@app.route('/index',methods=['GET','POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:

        snippet=str(request.form['snippet'])
        print(snippet)
        #Get embedded vector of the input

        text_vector=dbow.infer_vector(snippet.split(' '), epochs=100)

        #Predict vector using logistic Regresion

        y_pred = logreg.predict_proba([text_vector])
        best_n = np.argsort(y_pred, axis=1)[0]

        #Transform the best three classes to their respective file images names

        filenameList=["icons/{}.png".format(classes_dictionary[classDecoder[s]]) for s in best_n[-3:] ]
        s3,s2,s1=filenameList  

        topics=[str(classDecoder[s]) for s in best_n[-3:]]
        #Get the Keywords of the snippet

        string_=snippet.lower()
        key_words=keywords(string_).split('\n')

        return render_template('icons.html',s3=s3,s2=s2,s1=s1,t3=topics[0], t2=topics[1], t1=topics[2], keywords=key_words)




if __name__ == '__main__':
    app.run()
