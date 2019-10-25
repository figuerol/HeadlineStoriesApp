from flask import request,Blueprint, render_template, flash, redirect, url_for
from flask_bootstrap import __version__ as FLASK_BOOTSTRAP_VERSION
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from markupsafe import escape
from model import dbow, logreg, classDecoder, classes_dictionary
import numpy as np
import gensim
from gensim.summarization import keywords



frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def main():
    
    return redirect('/index')


@frontend.route('/index',methods=['GET','POST'])
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



