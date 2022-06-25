"""Game file."""

import random


def brain_even():
    """Game function."""
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        rand_num = random.randint(1, 100)
        print(f'Question: {rand_num}')
        answer = input('Your answer: ')
        if is_even(rand_num) and answer == 'yes':
            print('Correct!')
        elif not is_even(rand_num) and answer == 'no':
            print('Correct!')
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
    else:
        print('Congratulations!')


def is_even(num):
    """Check if 'num' is even. Returns True or False."""
    if num % 2 == 0:
        return True


if __name__ == '__main__':
    brain_even()
