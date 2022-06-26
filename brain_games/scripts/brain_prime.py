# !/usr/bin/env python3
"""Main game."""
from brain_games.games.brain_prime import brain_prime
from brain_games.logic import greeting


def main():
    """Play the game."""
    greeting()
    brain_prime()


if __name__ == '__main__':
    main()
