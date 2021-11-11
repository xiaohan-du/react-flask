def user_guess_once(target, dashes, inp):
    #  plot dashes based on user input, replace underline with matched char
    #  @param {target} the input string
    #  @param {dashes} the input dashes
    #  @param {inp} user input letter
    #  @return {dashes} underline where correct letters fill related position
    target = target.lower()

    if inp.isdigit():
        print('No digits allowed!')
    else:
        for idx, item in enumerate(target):
            if item == inp:
                dashes = dashes[:idx] + inp + dashes[idx + 1:]

    return dashes

def generate_pool(target):
    #  generate unique characters pool
    #  @param {target} the input string
    #  @return {pool} unsorted characters pool
    pool = set(list(target))
    return pool

def delete_the_guessed_word(target, word_list):
    word_list.remove(target)
    return word_list








# deleted methods

def plot_dashes(target):
    #  plot dashes based on {target} length, space is a space, target can be a phrase
    #  @param {target} the input string
    #  @return {dashes} a line of dashes, space is a space
    target = target.split(' ')
    dashes = ''
    for item in target:
        dashes = dashes + '-' * len(item) + ' '
    return dashes[:-1]

def get_categories(pool_data):
    #  get words categories
    #  @param {pool_data} the json data file content
    #  @return {categories} list of categories
    categories = []
    for item in pool_data:
        categories.append({'id': item['id'], 'category': item['category']})
    return categories

def get_category_details(pool_data, chosen_category):
    #  return chosen category information from {pool_data}
    #  @param {pool_data} the json data file content
    #  @param {chosen_category} the chosen category name
    #  @return {pool_data[candidate_id - 1]} the chosen category information
    for data in pool_data:
        if data['category'] == chosen_category:
            return data