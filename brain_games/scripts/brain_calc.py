# !/usr/bin/env python3
"""Main function of the game."""
from brain_games.logic import welcome_user
from brain_games.games.brain_calc import brain_calc


def main():
    """Main game."""
    welcome_user(brain_calc())
    


if __name__ == '__main__':
    main()