#!/usr/bin/python3

from pyrob.api import *

def up():
    while not wall_is_above():
        move_up()
        fill_cell()
        if wall_is_above():
            while not wall_is_beneath():
                move_down()        
            break

def left():
    while wall_is_beneath():
        move_left()           

@task(delay=0.01)
def task_6_6():
    while True:
        move_right()
        if not wall_is_above():
            up()

        if wall_is_on_the_right() and wall_is_beneath():
            left()
            break
            


if __name__ == '__main__':
    run_tasks()
