"""Greeting file."""
import prompt


def welcome_user():
    """Greeting function."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ').capitalize()
    print(f'Hello, {name}')


if __name__ == '__main__':
    welcome_user()
