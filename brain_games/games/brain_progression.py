"""File with a game."""

import random


def brain_progression():
    """Game function."""
    print('What number is missing in the progression?')
    for _ in range(3):
        start = random.randint(1, 100)
        step = random.randint(1, 5)
        length = random.randint(5, 10)
        lst_prog, correct = progression(start, step, length)
        print(f'Question: {lst_prog}')
        answer = int(input('Your answer: '))
        if correct == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
    else:
        print('Congratulations!')


def progression(start, step, length):
    """The function construct progression."""
    lst_prog = []
    rand_ind = random.randint(0, len(lst_prog) + 1)
    for i in range(length):
        if i == rand_ind:
            lst_prog.append('..')
            correct = start
        else:
            lst_prog.append(start)
        start += step
    return lst_prog, correct


if __name__ == '__main__':
    brain_progression()
