#!/usr/bin/python3

from pyrob.api import *

n = 27

def right(n):
    for i in range(n):
        move_right()
        fill_cell()
    move_down()
def left(n):
    for i in range(n):
        fill_cell()
        move_left()
    move_down()

@task(delay=0.05)
def task_4_3():
    for _ in range(6):
        right(n)
        left(n)
    move_right()
        


if __name__ == '__main__':
    run_tasks()
