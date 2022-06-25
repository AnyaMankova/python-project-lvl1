"""File with a game."""

import random


def brain_gcd():
    """Game function."""
    print('Find the greatest common divisor of given numbers.')
    for _ in range(3):
        rand_num1 = random.randint(1, 100)
        rand_num2 = random.randint(1, 100)
        print(f'Question: {rand_num1} {rand_num2}')
        answer = int(input('Your answer: '))
        correct = find_divisor(rand_num1, rand_num2)
        if correct == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
    else:
        print('Congratulations!')


def find_divisor(rand_num1, rand_num2):
    """Find the greatest common divisor."""
    if rand_num1 > rand_num2:
        for i in range(rand_num2, 0, -1):
            if rand_num1 % i == 0 and rand_num2 % i == 0:
                return i

    else:
        for i in range(rand_num1, 0, -1):
            if rand_num2 % i == 0 and rand_num1 % i == 0:
                return i


if __name__ == '__main__':
    brain_gcd()
