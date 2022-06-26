"""File with a game."""

from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START = 1
STOP = 100
DIV_START = 2


def game_options():
    """Game function."""
    task = randint(START, STOP)
    for i in range(DIV_START, task):
        if task % i == 0:
            correct_answ = 'no'
            break
    else:
        correct_answ = 'yes'
    return task, correct_answ
