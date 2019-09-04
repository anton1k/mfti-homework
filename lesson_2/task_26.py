#!/usr/bin/python3

from pyrob.api import *

def plus():
    move_right()
    
    fill_cell()
    move_down()

    fill_cell()
    move_down()

    fill_cell()
    move_up()

    move_right()
    fill_cell()

    move_left(2)
    fill_cell()

    move_up()

def right_left(flag, stop):
    plus()
    for _ in range(9):
        if flag == 'right':
            move_right(4)
        else:
            move_left(4)
        plus()

    if stop < 0:
        move_down(4)

@task(delay=0.02)
def task_2_4():
    while True:
        for _ in range(2):
            right_left('right', -1)
            right_left('left', -1)

        right_left('right', 1)

        while not wall_is_on_the_left():
            move_left()

        break


if __name__ == '__main__':
    run_tasks()
