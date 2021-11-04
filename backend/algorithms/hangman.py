import json, random
from algorithms import algorithmFunctions as af

with open('data/test_pool.json') as f:
    target_pool = json.load(f)

pool_data = target_pool['targets']
categories = af.get_categories(pool_data)
target_data = af.chooose_a_category(pool_data)
word_list = target_data['words']


def hangman():
    target = random.choice(word_list)
    dashes = af.plot_dashes(target)
    return dashes