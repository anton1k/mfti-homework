#!/usr/bin/python3

from pyrob.api import *



def plus():
    for _ in range(3):
        move_down()
        fill_cell()

    move_up()

    move_right()
    fill_cell()

    move_left(2)
    fill_cell()

@task
def task_2_2():
    while True:
        move_right()
        plus()

        for _ in range(4):
            move_up(2)
            move_right(5)
            plus()

        move_up()
        break


if __name__ == '__main__':
    run_tasks()
