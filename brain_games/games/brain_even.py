"""Game file."""
import prompt
import random


def brain_even():
    """Game function."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ').capitalize()
    print(f'Hello, {name}')

    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        rand_num = random.randint(1, 100)
        print(f'Question: {rand_num}')
        answer = input('Your answer: ')
        if (is_even(rand_num) and answer == 'yes') or (not is_even(rand_num) and answer == 'no'):
            print('Correct!')
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
    else:
        print(f'Congratulations, {name}!')


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    brain_even()