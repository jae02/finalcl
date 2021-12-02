#-*- coding: utf-8 -*-
from flask import Flask , render_template , request
from flask_cors import CORS
import json
import os
import util
import ast



app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/' , methods=['GET', 'POST'])
def search():
    return render_template("index.html")

app.run(host='0.0.0.0' , port = 5100 , debug=True)