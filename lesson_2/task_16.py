#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
    while not wall_is_above():
        move_up()

        if wall_is_above() and wall_is_on_the_right() and not wall_is_beneath():
            while not wall_is_on_the_left():
                move_left()

        if wall_is_above() and wall_is_on_the_left() and not wall_is_beneath():
            while not wall_is_on_the_right():
                move_right()


if __name__ == '__main__':
    run_tasks()
