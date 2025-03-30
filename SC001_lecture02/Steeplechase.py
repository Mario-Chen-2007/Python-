"""
File: Steeplechase.py
Name: Mario
---------------------------------
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


def jump():
    """
    Pre-condition: Karel is on left side of the wall, facing East
    Post-condition: Karel is on right side of the wall
    """
    up()
    cross()
    down()


def up():
    """
    Pre-condition: Karel is on left side of the wall, facing East
    Post-condition: Karel is at the upper left side of the wall
    """
    turn_left()
    while not right_is_clear():
        move()


def cross():
    """
    Pre-condition: Karel is at the upper left side of the wall
    Post-condition: Karel cross over the wall and facing south
    """
    turn_R()
    move()
    turn_R()


def down():
    """
    Pre-condition: Karel cross over the wall and facing south
    Post-condition: Karel go down to the button of wall and facing East
    """
    while front_is_clear():
        move()
    if not front_is_clear():
        turn_left()


    #alternative
    # while not front_is_clear():
    #     turn_left()
    #     move()
    #     turn_R()


def turn_R():
    for i in range(3):
        turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
