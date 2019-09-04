#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    while True:
        if cell_is_filled():
            move_left()
            if cell_is_filled():
                break
            else:
                move_right(2)
                break
        move_up()
            


if __name__ == '__main__':
    run_tasks()
