#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():

    n = 12

    def down():
        move_right()
        move_down()
        while True:
            if wall_is_beneath():
                move_right()
                break
            fill_cell()
            move_down()

    def up(n):
        for _ in range(n):
            move_up()
            fill_cell()
        

    while True:
        for _ in range(7):
            down()
            up(n)
            n = n - 2
        move_left(13)
        break
   


if __name__ == '__main__':
    run_tasks()
