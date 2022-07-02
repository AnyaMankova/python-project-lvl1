"""Logic for every game in the programme."""

import prompt

GREETING = 'Welcome to the Brain Games!'
NAME_REQUEST = 'May I have your name? '
SAY_HELLO = 'Hello, {}!'
COUNT_OF_ROUNDS = 3
TASK = 'Question: {}'
ANSWER = 'Your answer: '
CORRECT = 'Correct!'
WRONG = "'{}' is wrong answer ;(.\nCorrect answer was '{}'.\nLet's try again, {}!"
WIN_MSG = 'Congratulations, {}!'


def logic(game):
    """Describe main logic."""
    print(GREETING)
    name = prompt.string(NAME_REQUEST).capitalize()
    print(SAY_HELLO.format(name))
    print(game.DESCRIPTION)
    score = 0

    while score < COUNT_OF_ROUNDS:
        task, correct_answ = game.game_options()
        print(TASK.format(task))
        user_answer = prompt.string(ANSWER)
        if user_answer == correct_answ:
            print(CORRECT)
            score += 1
        else:
            print(WRONG.format(user_answer, correct_answ, name))
            break
    if score == COUNT_OF_ROUNDS:
        print(WIN_MSG.format(name))
