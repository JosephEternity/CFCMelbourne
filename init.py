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
from flasktext.kvsession import KVSessionExtension

APPLICATION_NAME = 'CFC Melbourne Website'

app = flask.Flask(__name__)
# encrypt sessions with secret key.
app.secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits)
                         for x in xrange(32))

store = DictStore()

KVSessionExtension(store,app)

class View(flask.views.MethodView):
	def get(self):
		return render_template('index.html')

app.add_url_rule('/',view_func=View.as_view('main'))

app.debug = True
app.run()
