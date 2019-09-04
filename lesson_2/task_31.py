#!/usr/bin/python3

from pyrob.api import *

flag = True

def left():
    while not wall_is_on_the_left():
        move_left()
        if not wall_is_beneath():          
            down()


def right():
    while not wall_is_on_the_right():
        if not wall_is_beneath():
            down()
            break
        move_right()
    else:
        left()

def down():
    while not wall_is_beneath():
        move_down()
    else:
        right() 


@task(delay=0.01)
def task_8_30():
    down()

if __name__ == '__main__':
    run_tasks()
