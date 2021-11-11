# from flask import Flask, send_from_directory
# from flask_restful import Api, Resource, reqparse
# from flask_cors import CORS #comment this on deployment
# from api.ApiHandler import ApiHandler

# app = Flask(__name__, static_url_path='', static_folder='frontend/build')

# api = Api(app)

# @app.route("/", defaults={'path':''})
# def serve(path):
#     return send_from_directory(app.static_folder,'index.html')

# api.add_resource(ApiHandler, '/flask')

from flask_cors import CORS #comment this on deployment
from flask import Flask, request
from algorithms import algorithmFunctions as af
from algorithms import hangman as hm
import json

with open('data/test_pool.json') as f:
    target_pool = json.load(f)

app = Flask(__name__)
CORS(app) #comment this on deployment

pool_data = target_pool['targets']
categories = af.get_categories(pool_data)

@app.route('/', methods = ['GET'])
def home():
    if request.method == 'GET':
        return {
            'categories': categories
        }

@app.route('/<chosen_category>', methods = ['GET', 'POST'])
def get_word_from_chosen_category(chosen_category):
    if request.method == 'POST':
        # key_press = request.get_json(silent=True)['keyPress']
        chosen_category = request.get_json(silent=True)['chosenCategory']
        category_details = af.get_category_details(pool_data, chosen_category)
        dashes, target = hm.hangman(category_details)
        return {
            'dashes': dashes,
            'target': target
        }