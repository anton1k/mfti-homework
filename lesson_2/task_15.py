#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    while True:
        if wall_is_above() and wall_is_on_the_left():
            for _ in range(9):
                move_down()
                move_right()
            break
        
        if wall_is_above() and wall_is_on_the_right():
            for _ in range(9):
                move_down()
                move_left()
            break

        if wall_is_beneath() and wall_is_on_the_left():
            for _ in range(9):
                move_up()
                move_right()
            break
        
        if wall_is_beneath() and wall_is_on_the_right():
            for _ in range(9):
                move_up()
                move_left()
            break


if __name__ == '__main__':
    run_tasks()
