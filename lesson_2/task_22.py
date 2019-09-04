#!/usr/bin/python3

from pyrob.api import *
def right():
    if not wall_is_above():
        move_down()
    while not wall_is_on_the_right():
        fill_cell()
        move_right()
        fill_cell()

def left():
    if not wall_is_beneath():
        move_down()
    while not wall_is_on_the_left():
        fill_cell()
        move_left()
        fill_cell()
            


@task
def task_5_10():
    while True:
        if wall_is_beneath() \
        and wall_is_on_the_left() \
        and wall_is_above() \
        and wall_is_on_the_right():
            fill_cell()
            break
        right()
        left()
        if wall_is_beneath() and wall_is_on_the_left():
            break


if __name__ == '__main__':
    run_tasks()
