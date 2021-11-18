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
    hangman.guessed = []
    if request.method == 'GET':
        return f'Chosen category is {chosen_category_name}, target is {hangman.target}'
    elif request.method == 'POST':
        chosen_category_name = request.get_json(silent=True)['chosenCategory']
        hangman.get_and_plot_dashes()
        return {
            'dashes': hangman.dashes,
            'target': hangman.target
        }

@app.route('/keyup', methods = ['POST'])
def verify_keyup():
    if request.method == 'POST':
        key_up = request.get_json(silent=True)['keyUp']
        hangman.guessed = list(set(hangman.guessed))
        if key_up in hangman.guessed:
            hangman.message = 'Already guessed this letter!'
        else:
            hangman.user_guess_once(key_up)
            hangman.guessed.append(key_up)
            hangman.message = ''
        return {
            'message': hangman.message,
            'dashes': hangman.dashes,
            'guessed': hangman.guessed
        }
