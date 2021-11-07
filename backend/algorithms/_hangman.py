from algorithmFunctions import *
import json, random

is_play = None

with open('../data/test_pool.json') as f:
    target_pool = json.load(f)

pool_data = target_pool['targets']
# get category and its id
pool_length = len(pool_data)

target_data = choose_a_category(pool_data)

print(f"Your chosen category is: {target_data['id']} -- {target_data['category']}")
print(f"Difficulty: {target_data['difficulty']}")

word_list = target_data['words']

while is_play not in ('yes', 'no') and len(word_list) != 0:
    is_play = input('Start game? (y=Yes/n=No) ')
    if is_play == 'y':

        target = random.choice(word_list)

        word_list = delete_the_guessed_word(target, word_list)

        iterations = len(target) - target.count(' ')

        dashes = plot_dashes(target)

        pool = generate_pool(target)

        guessed = []

        dashes_remain = len(dashes)

        while iterations > 0:
            inp = input('Please type a letter in lower case: ')
            guessed = list(set(guessed))

            if dashes_remain == 0:
                iterations = 0
                print('Dead')

            elif inp in pool:
                dashes = user_guess_once(target, dashes, inp)
                correct_num = dashes.count(inp)
                iterations -= correct_num
                pool.remove(inp)
                guessed.append(inp)
                print(dashes)

            elif len(inp) > 1:
                print('Only 1 letter allowed each time!')

            elif isinstance(inp, str) == False:
                print('Only letters allowed!')

            elif inp in guessed:
                guessed.append(inp)
                print('Already guessed!')

            else:
                guessed.append(inp)
                dashes_remain -= 1
                print(f'Closer to death, {dashes_remain} steps left')

    elif is_play == 'n':
        break
