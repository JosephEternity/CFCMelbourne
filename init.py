__author__ = 'joseph.eternity@gmail.com (Vinay Joseph)'

import json
import random
import string


import flask, flask.views
from flask import render_template
from flask import make_response
from flask import request
from flask import session


from simplekv.memory import DictStore
from flaskext.kvsession import KVSessionExtension

APPLICATION_NAME = 'CFC Melbourne Website'

app = flask.Flask(__name__)
# encrypt sessions with secret key.
app.secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits)
                         for x in xrange(32))

store = DictStore()

#app session handling..
KVSessionExtension(store,app)

# Update client_secrets.json with your Google API project information.
# Do not change this assignment.
CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']


@app.route('/',methods=['GET'])
def index():
	""" Initialize a session for the current user, and render index.html"""
	# Create a state token to prevent forgery of the request
	# Store it in the session for latter validation
	state= "".join(random.choice(string.ascii_uppercase + string.digits)
					for x in xrange(32))
	session['state'] = state
	# Set the client ID, Token State, and Application Name in the HTML while 
	# serving it.
	response = make_response(render_template('index.html',
											CLIENT_ID=CLIENT_ID,
											STATE=state,
											APPLICATION_NAME=APPLICATION_NAME))
	response.headers['Content-Type'] = 'text/html'
	return response
	

app.debug = True
app.run()