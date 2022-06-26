# !/usr/bin/env python3
"""Main game."""
from brain_games.games import brain_prime
from brain_games.logic import logic


def main():
    """Play the game."""
    logic(brain_prime)


if __name__ == '__main__':
    main()
