# !/usr/bin/env python3
"""Main function of the game."""
from brain_games.games import brain_calc
from brain_games.logic import logic


def main():
    """Play the game."""
    logic(brain_calc)


if __name__ == '__main__':
    main()
