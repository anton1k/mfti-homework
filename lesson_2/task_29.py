#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    while not wall_is_on_the_right():

        move_right()

        if cell_is_filled() and not wall_is_on_the_right():
            move_right()
            if cell_is_filled() and not wall_is_on_the_right():
                move_right()
                if cell_is_filled():
                    break


if __name__ == '__main__':
    run_tasks()
