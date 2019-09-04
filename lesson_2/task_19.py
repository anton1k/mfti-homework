#!/usr/bin/python3

from pyrob.api import *
def ext():
    while True:
        if not wall_is_above() or (wall_is_on_the_left() and not wall_is_above()):
            move_up()
        if wall_is_on_the_left() and wall_is_above():
             break
        if wall_is_above():
            move_left()

@task
def task_8_29():
    while True:
        if not wall_is_on_the_left():
            move_left()

        if wall_is_on_the_left() and not wall_is_beneath() and not wall_is_above():
            ext()
            break

        if wall_is_on_the_left() and wall_is_beneath() and wall_is_above():
            while True:
                if wall_is_on_the_right() and not wall_is_beneath() and not wall_is_above():
                    ext()
                    break
                if wall_is_on_the_right() and wall_is_beneath() and wall_is_above():
                    break
                move_right()

            break


if __name__ == '__main__':
    run_tasks()
