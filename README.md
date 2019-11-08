# HeadlineStoriesApp
This is an app which predicts the topic/newspaper-section from a body of text. The working app can be found at https://headlinestoriesapp.herokuapp.com .

The jupyter notebook used to train the model running behind can be found in app/HeadlineStories_build_model . The model architecture and small parts of the code 
are based on Susan Li's  article on Medium "Multi-Class Text Classification with Doc2Vec & Logistic Regression", which is a great read and I highly recommend.
The model was trained on the lead paragraphs of 400,000 articles obtained from the New York Times API. 

The app delivers the prediction results in terms of Icons, which were obtained from The Noun Project. Every Icon used is credited to the author in the image, as per the license agreement in The Noun Project.
Thier work is truly inspirational and the platform is a great way for designers across the world to showcase their work.

This app was built using a flask framework. The main file building it can be found in app/frontend.py .




