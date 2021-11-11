import random

class Hangman:
    def __init__(self, pool_data):
        self.pool_data = pool_data

    def get_categories(self):
        #  get words categories
        #  @return {categories} list of category id and content
        categories = []
        for item in self.pool_data:
            categories.append({'id': item['id'], 'category': item['category']})
        return categories

    def get_target(self, chosen_category_name):
        #  get a random target word
        #  @param {chosen_category_name} the chose category name
        #  @return {data} the chosen category details
        for data in self.pool_data:
            if data['category'] == chosen_category_name:
                return random.choice(data['words'])

    def plot_dashes(self, target):
        #  plot dashes based on {target} length, space is a space, target can be a phrase
        #  @param {target} the target word
        #  @return {dashes} a line of dashes, space is a space
        target = target.split(' ')
        dashes = ''
        for item in target:
            dashes = dashes + '-' * len(item) + ' '
        return dashes[:-1]

