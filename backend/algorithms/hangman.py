import json, random
from algorithms import algorithmFunctions as af

with open('data/test_pool.json') as f:
    target_pool = json.load(f)

pool_data = target_pool['targets']
categories = af.get_categories(pool_data)
category = af.get_category_details(pool_data, 'animals')

def hangman(category):
    targets = category['words']
    target = random.choice(targets)
    dashes = af.plot_dashes(target)
    return dashes, target