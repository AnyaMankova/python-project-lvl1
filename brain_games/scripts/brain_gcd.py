# !/usr/bin/env python3
"""Main game."""
from brain_games.games.brain_gcd import brain_gcd
from brain_games.logic import greeting


def main():
    """Play the game."""
    greeting()
    brain_gcd()


if __name__ == '__main__':
    main()
