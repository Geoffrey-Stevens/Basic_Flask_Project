#importing flask class from flask.py file
from flask import Flask

#creating an instance of rthe flask class, in order to run this application
#name parameter will default to folder name
app = Flask(__name__)

#from teh app folder import the routes.py file and start up at the index route
from app import routes
