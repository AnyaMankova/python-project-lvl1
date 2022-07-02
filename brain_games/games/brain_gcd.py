"""File with a game."""

import random
DESCRIPTION = 'Find the greatest common divisor of given numbers.'
START = 1
STOP = 100
STEP = -1


def game_options():
    """Game function."""
    rand_num1 = random.randint(START, STOP)
    rand_num2 = random.randint(START, STOP)
    task = f'{rand_num1} {rand_num2}'
    if rand_num1 > rand_num2:
        for div in range(rand_num2, 0, STEP):
            if rand_num1 % div == 0 and rand_num2 % div == 0:
                correct_answ = div
                break
    else:
        for div in range(rand_num1, 0, STEP):
            if rand_num2 % div == 0 and rand_num1 % div == 0:
                correct_answ = div
                break
    return task, str(correct_answ)
