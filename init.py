#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   init.py
@Time    :   2023/03/16 22:09:09
@Author  :   Serein
@Version :   1.0
@Contact :   serein7z@163.com
@License :   (C)Copyright 2022-2023, USTB_MedicalAI
@Desc    :   {initialize the window}
'''
import tkinter as tk
from utils import *


def init(mouse):
    root = tk.Tk()
    #* 设置主窗口大小
    root.geometry("1440x720")
    root.title('Turtle with Mouse')

    #* 创建左侧窗口
    canvas = tk.Canvas(root, width=720, height=720)
    canvas.pack(side="left", fill="both", expand=True)

    #* 创建右侧窗口
    turtle_canvas = tk.Canvas(root, width=720, height=720)
    turtle_canvas.pack(side="right", fill="both", expand=True)
    set_button(canvas, turtle_canvas, mouse, 'Circle', circle_status, 0, 0)
    set_button(canvas, turtle_canvas, mouse, 'Clear', clear, 0, 30, True)
    set_button(canvas, turtle_canvas, mouse, 'Draw', normal_status, 0, 60)
    set_button(canvas, turtle_canvas, mouse, 'RecTangle', Rect_status, 0, 90)
    root.grid_columnconfigure(0)
    root.grid_rowconfigure(0)
    return root, canvas, turtle_canvas


def set_button(canvas, turtle_canvas, mouse, text, func, x, y, flag=False):
    if flag:
        button = tk.Button(canvas, text=text, command=lambda: func(canvas, turtle_canvas, mouse), width=8, height=1)
    else:
        button = tk.Button(canvas, text=text, command=lambda: func(mouse), width=8, height=1)
    button.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    button.place(x=x, y=y)
    return button


def init_turtle(canvas, speed, bgcolor='white', pencolor='red', pensize=2):
    screen = turtle.TurtleScreen(canvas)
    screen.setworldcoordinates(0, 720, 720, 0)
    screen.bgcolor(bgcolor)
    t = turtle.RawTurtle(screen)
    t.pencolor(pencolor)
    t.pensize(pensize)
    t.speed(speed)
    # t.down()
    # t.goto(20, 50)
    t.hideturtle()
    return t
