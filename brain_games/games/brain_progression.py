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
    rand_ind = random.randint(0, length)
    lst_prog, correct_answ, task = [], '', ''
    for i in range(length):
        lst_prog.append(str(prog_start))
        prog_start += prog_step
    correct_answ = lst_prog.pop(rand_ind)
    lst_prog.insert(rand_ind, '..')
    task = (' ').join(lst_prog)
    return task, str(correct_answ)
