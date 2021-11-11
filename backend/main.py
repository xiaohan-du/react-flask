from flask_cors import CORS #comment this on deployment
from flask import Flask, request
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
        hangman.get_categories()
        return {
            'categories': hangman.categories
        }

@app.route('/<chosen_category_name>', methods = ['GET', 'POST'])
def get_word_from_chosen_category(chosen_category_name):
    hangman.get_target(chosen_category_name)
    if request.method == 'GET':
        return f'Chosen category is {chosen_category_name}, target is {hangman.target}'
    elif request.method == 'POST':
        # key_press = request.get_json(silent=True)['keyPress']
        chosen_category_name = request.get_json(silent=True)['chosenCategory']
        hangman.get_and_plot_dashes()
        return {
            'dashes': hangman.dashes,
            'target': hangman.target
        }

@app.route('/keypress', methods = ['POST'])
def verify_keypress():
    if request.method == 'POST':
        key_press = request.get_json(silent=True)['keyPress']
        hangman.user_guess_once(key_press)
        return {
            'dashes': hangman.dashes
        }
