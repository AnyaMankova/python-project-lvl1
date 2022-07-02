"""File with a game."""

import random
DESCRIPTION = 'What number is missing in the progression?'
START = 1
STOP = 100
MAX_STEP = 5
MIN_LEN = 5
MAX_LEN = 10


def game_options():
    """Game function."""
    prog_start = random.randint(START, STOP)
    prog_step = random.randint(START, MAX_STEP)
    length = random.randint(MIN_LEN, MAX_LEN)
    rand_ind = random.randint(0, length + 1)
    lst_prog = []
    for i in range(length):
        if i == rand_ind:
            lst_prog.append('..')
            correct_answ = prog_start
        else:
            lst_prog.append(prog_start)
        prog_start += prog_step
    task = lst_prog
    return (*task), str(correct_answ)
