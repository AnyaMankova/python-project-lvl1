"""File with a game."""

import random
DESCRIPTION = 'What is the result of the expression?'
START = 1
STOP = 100
OPERATOR_LST = ['+', '*', '-']


def game_options():
    """Game function."""
    rand_num1 = random.randint(START, STOP)
    rand_num2 = random.randint(START, STOP)
    rand_operator = random.choice(OPERATOR_LST)
    task = f'{rand_num1} {rand_operator} {rand_num2}'
    if rand_operator == '+':
        correct_answ = rand_num1 + rand_num2
    elif rand_operator == '*':
        correct_answ = rand_num1 * rand_num2
    elif rand_operator == '-':
        correct_answ = rand_num1 - rand_num2
    return task, str(correct_answ)
