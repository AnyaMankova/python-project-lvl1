# !/usr/bin/env python3
"""Main game."""
from brain_games.games import brain_progression
from brain_games.logic import logic


def main():
    """Play the game."""
    logic(brain_progression)


if __name__ == '__main__':
    main()
