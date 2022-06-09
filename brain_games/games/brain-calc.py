"""Greeting file."""
import prompt
import random
from brain_games.logic import name


DESCRIPTION = 'What is the result of the expression?'

def brain_calc():
    """Game function."""

    print(DESCRIPTION)
    for _ in range(3):
        rand_num1 = random.randint(1, 100)
        rand_num2 = random.randint(1, 100)
        rand_operator = random.choice['+', '*', '-']
        print(f'Question: {rand_num1} + {rand_operator} + {rand_num2}')
        answer = int(input('Your answer: '))
        correct = result(rand_num1, rand_num2, rand_operator)
        if correct == answer:
            print('Correct!')
        else:
            print("'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
    else:
        print(f'Congratulations, {name}!')


def result(a, b, c):
    if c == ' +':
        return a + b
    elif c == '*':
        return a * b
    elif c == '-':
        return a - b


if __name__ == '__main__':
    brain_calc()
