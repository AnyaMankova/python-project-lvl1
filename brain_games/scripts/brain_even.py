# !/usr/bin/env python3
"""Main game."""
from brain_games.games.brain_even import brain_even
from brain_games.logic import greeting


def main():
    """Play the game."""
    greeting()
    brain_even()


if __name__ == '__main__':
    main()
