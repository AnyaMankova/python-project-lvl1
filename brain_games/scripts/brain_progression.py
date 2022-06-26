# !/usr/bin/env python3
"""Main game."""
from brain_games.games.brain_progression import brain_progression
from brain_games.logic import greeting


def main():
    """Play the game."""
    greeting()
    brain_progression()


if __name__ == '__main__':
    main()
