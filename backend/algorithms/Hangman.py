import random

class Hangman:
    def __init__(self, pool_data):
        self.pool_data = pool_data
        self.target = ''
        self.dashes = ''
        self.categories = []
        self.guessed = []
        self.message = ''

    def get_categories(self):
        #  get words categories
        #  @return {categories} list of category id and content
        categories = []
        for item in self.pool_data:
            categories.append({'id': item['id'], 'category': item['category']})
        self.categories = categories

    def get_target(self, chosen_category_name):
        #  get a random target word
        #  @param {chosen_category_name} the chose category name
        #  @return {data} the chosen category details
        for data in self.pool_data:
            if data['category'] == chosen_category_name:
                self.target = random.choice(data['words'])

    def get_and_plot_dashes(self):
        #  plot dashes based on {target} length, space is a space, target can be a phrase
        #  @param {target} the target word
        #  @return {dashes} a line of dashes, space is a space
        target = self.target.split(' ')
        dashes = ''
        for item in target:
            dashes = dashes + '-' * len(item) + ' '
        self.dashes = dashes[:-1]

    def user_guess_once(self, inp):
        #  plot dashes based on user input, replace underline with matched char
        #  @param {target} the input string
        #  @param {dashes} the input dashes
        #  @param {inp} user input letter
        #  @return {dashes} underline where correct letters fill related position
        target = self.target.lower()

        dashes = self.dashes
        
        if inp.isdigit():
            return 'No digits allowed'
        else:
            for idx, item in enumerate(target):
                if item == inp:
                    dashes = dashes[:idx] + inp + dashes[idx + 1:]
        self.dashes = dashes
