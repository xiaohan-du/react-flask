from flask_cors import CORS #comment this on deployment
from flask import Flask, request
from algorithms import algorithmFunctions as af
from algorithms.Hangman import Hangman
import json

with open('data/test_pool.json') as f:
    target_pool = json.load(f)

hangman = Hangman(target_pool['targets'])

app = Flask(__name__)
CORS(app) #comment this on deployment

@app.route('/', methods = ['GET'])
def home():
    if request.method == 'GET':
        return {
            'categories': hangman.get_categories()
        }

@app.route('/<chosen_category_name>', methods = ['GET', 'POST'])
def get_word_from_chosen_category(chosen_category_name):
    if request.method == 'POST':
        # key_press = request.get_json(silent=True)['keyPress']
        chosen_category_name = request.get_json(silent=True)['chosenCategory']
        target = hangman.get_target(chosen_category_name)
        dashes = hangman.plot_dashes(target)
        return {
            'dashes': dashes,
            'target': target
        }