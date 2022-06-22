# !/usr/bin/env python3
"""Main function of the game."""
from brain_games.games.brain_calc import brain_calc
from brain_games.logic import greeting


def main():
    """Play the game."""
    greeting()
    brain_calc()


if __name__ == '__main__':
    main()
