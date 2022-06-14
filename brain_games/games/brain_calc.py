"""File with a game."""

import random
import prompt


def brain_calc():
    """Game function."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ').capitalize()
    print(f'Hello, {name}')
    print('What is the result of the expression?')
    for _ in range(3):
        rand_num1 = random.randint(1, 100)
        rand_num2 = random.randint(1, 100)
        operator_lst = ['+', '*', '-']
        rand_operator = random.choice(operator_lst)
        print(f'Question: {rand_num1} {rand_operator} {rand_num2}')
        answer = int(input('Your answer: '))
        correct = math_expression(rand_num1, rand_num2, rand_operator)
        if correct == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
    else:
        print(f'Congratulations, {name}!')


def math_expression(rand_num1, rand_num2, rand_operator):
    """Calculate expression.
    rand_num1, rand_num2 are random numbers, rand_operator is to calculate expression."""
    if rand_operator == '+':
        return rand_num1 + rand_num2
    elif rand_operator == '*':
        return rand_num1 * rand_num2
    elif rand_operator == '-':
        return rand_num1 - rand_num2


if __name__ == '__main__':
    brain_calc()
