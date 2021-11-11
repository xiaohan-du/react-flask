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
