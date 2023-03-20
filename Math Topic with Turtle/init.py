#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   init.py
@Time    :   2023/03/20 10:52:59
@Author  :   Serein
@Version :   1.0
@Contact :   serein7z@163.com
@License :   (C)Copyright 2022-2023, USTB_MedicalAI
@Desc    :   {initialization}
'''

import turtle


def init_turtle(speed, pensize=3, hide=True):
    screen = turtle.Screen()
    screen.title("Mathematical Calculation")
    screen.bgcolor("white")
    # screen.setup(800, 800, 0, 0)
    screen.tracer(0)
    t = turtle.Turtle()
    # turtle.setup(800, 800, 0, 0)
    t.speed(speed)
    t.pensize(pensize)
    t.up()
    if hide:
        t.hideturtle()
    # print(screen.window_height(), screen.window_width())
    return t, screen
