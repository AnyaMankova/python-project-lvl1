"""Game file."""

import random
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
START = 1
STOP = 100


def game_options():
    """Game function."""
    rand_num = random.randint(START, STOP)
    task = rand_num
    if rand_num % 2 == 0:
        correct_answ = 'yes'
    else:
        correct_answ = 'no'
    return task, correct_answ
