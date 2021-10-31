from functions import *
import json

is_play = None

with open('../data/target_pool.json') as f:
    target_pool = json.load(f)

pool_data = target_pool['targets']
# get category and its id
pool_length = len(pool_data)

chooose_and_delete_a_word(pool_data)

# while is_play not in ('yes', 'no'):
#     is_play = input('Start game? (y=Yes/n=No) ')
#     if is_play == 'y':

#         target = random.choice(target_pool)

#         iterations = len(target) - target.count(' ')

#         underlines = plot_underlines(target)

#         pool = generate_pool(target)

#         guessed = []

#         underlines_remain = len(underlines)

#         while iterations > 0:
#         inp = input('Please type a letter in lower case: ')
#         guessed = list(set(guessed))

#         if underlines_remain == 0:
#             iterations = 0
#             print('Dead')

#         elif inp in pool:
#             underlines = user_guess_once(target, underlines, inp)
#             correct_num = underlines.count(inp)
#             iterations -= correct_num
#             pool.remove(inp)
#             guessed.append(inp)
#             print(underlines)

#         elif len(inp) > 1:
#             print('Only 1 letter allowed each time!')

#         elif isinstance(inp, str) == False:
#             print('Only letters allowed!')

#         elif inp in guessed:
#             guessed.append(inp)
#             print('Already guessed!')

#         else:
#             guessed.append(inp)
#             underlines_remain -= 1
#             print(f'Closer to death, {underlines_remain} steps left')

# elif is_play == 'n':
#     break
