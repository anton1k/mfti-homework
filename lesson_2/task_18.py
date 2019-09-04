#!/usr/bin/python3

from pyrob.api import *

def ext():
    while True:
        if not wall_is_above():
            move_up()
        if wall_is_on_the_left():
             break
        if wall_is_above():
            move_left()
@task
def task_8_28():
    while True:
        if not wall_is_above():
            ext()
            break

        if not wall_is_above() and wall_is_on_the_right():
            ext()
            break

        if not wall_is_on_the_left():
            move_left()
        if wall_is_on_the_left():
            if not wall_is_above():
                ext()
                break
            move_right()
            while True:
                if not wall_is_above():
                    ext()
                    break
                if not wall_is_on_the_right():
                    move_right()
                if not wall_is_above() and wall_is_on_the_right():
                    ext()
                    break
                if wall_is_on_the_right():
                    break
            break


if __name__ == '__main__':
    run_tasks()
