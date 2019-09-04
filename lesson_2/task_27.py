#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    n = 0
    for _ in range(1):
        move_right()
        fill_cell()
        
    while not wall_is_on_the_right():

        for _ in range(n):
            move_right()
            if wall_is_on_the_right():
                break

        if not wall_is_on_the_right():
            fill_cell()
        n+=1

if __name__ == '__main__':
    run_tasks()
