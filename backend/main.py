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
from flask import Flask
from algorithms import algorithmFunctions as af
import json

with open('data/test_pool.json') as f:
    target_pool = json.load(f)

app = Flask(__name__)
CORS(app) #comment this on deployment

pool_data = target_pool['targets']
categories = af.get_categories(pool_data)
dashes = af.plot_dashes('hello world')

@app.route('/', methods = ['GET'])
def get_dashes():
    return {
        'dashes': dashes,
        'categories': categories
    }
