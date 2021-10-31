import random


def plot_underlines(target):
    #  plot dashes based on {target} length, space is a space, target can be a phrase
    #  @param {target} the input string
    #  @return {underlines} a line of underlines, space is a space
    target = target.split(' ')
    underlines = ''
    for item in target:
        underlines = underlines + '_' * len(item) + ' '
    return underlines[:-1]


def user_guess_once(target, underlines, inp):
    #  plot dashes based on user input, replace underline with matched char
    #  @param {target} the input string
    #  @param {underlines} the input underlines
    #  @param {inp} user input letter
    #  @return {underlines} underline where correct letters fill related position
    target = target.lower()

    if inp.isdigit():
        print('No digits allowed!')
    else:
        for idx, item in enumerate(target):
            if item == inp:
                underlines = underlines[:idx] + inp + underlines[idx + 1:]

    return underlines


def generate_pool(target):
    #  generate unique characters pool
    #  @param {target} the input string
    #  @return {pool} unsorted characters pool
    pool = set(list(target))
    return pool


def chooose_and_delete_a_word(pool_data):
    #  choose a word, oncec guess is complete, delete it from the list
    #  chosen id being removed first, then chosen word is removed
    #  @param {target_pool} the json data file content
    #  @return {target} the target word to be guessed
    pool_length = len(pool_data)
    id_list = list(range(pool_length))
    id_list = [item + 1 for item in id_list]
    candidate_id = id_list[random.randrange(0, pool_length)]
    print(f"Your chosen category is {pool_data[candidate_id - 1]['category']}")
    print(f"Difficulty: {pool_data[candidate_id - 1]['difficulty']}")
    id_list = id_list.remove(candidate_id)
    return candidate_id
