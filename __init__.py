from flask import Flask
from flask_bootstrap import Bootstrap
from frontend import frontend


# http://flask.pocoo.org/docs/patterns/appfactories/
def create_app(configfile=None):

    app = Flask(__name__)
    Bootstrap(app)
    app.register_blueprint(frontend)

    return app
