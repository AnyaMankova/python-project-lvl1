"""File with a game."""

import random


def brain_prime():
    """Game function."""
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(3):
        rand_num = random.randint(1, 100)
        print(f'Question: {rand_num}')
        answer = input('Your answer: ')
        correct = is_prime(rand_num)
        if correct == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
    else:
        print('Congratulations!')


def is_prime(rand_num):
    """Is number prime or not."""
    count = 0
    for i in range(2, rand_num):
        if rand_num % i == 0:
            count += 1
            correct = 'no'
            break
    else:
        correct = 'yes'
    return correct


if __name__ == '__main__':
    brain_prime()
