#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   turtle_with_mouse.py
@Time    :   2023/03/15 10:45:49
@Author  :   Serein
@Version :   1.0
@Contact :   serein7z@163.com
@License :   (C)Copyright 2022-2023, USTB_MedicalAI
@Desc    :   {turtle with your mouse! guided by chatgpt}
'''
from tkinter import *
import turtle as t


class Turtle:
    def __init__(self, master, turtle):
        self.master = master
        self.master.bind("<Key>", self.go_turtle)
        self.mouse_moves = mouse_moves
        self.turtle = turtle

    def go_turtle(self, event):
        print('working')
        self.turtle.up()
        print(self.mouse_moves)
        # start_x, start_y = mouse_moves[0]
        # self.turtle.goto(start_x, start_y)
        for x, y in self.mouse_moves:
            self.turtle.goto(x - 360, -(y - 250))
            self.turtle.down()


# root = Tk()
# app = App(root)
# root.mainloop()
import tkinter as tk
# 创建一个主窗口
root = tk.Tk()

# 设置主窗口大小
root.geometry("1440x900")

canvas = tk.Canvas(root, width=720, height=450)
canvas.pack(side="left", fill="both", expand=True)
global mouse_moves
mouse_moves = []


def down(event):
    mouse_moves.append((event.x, event.y))


# 移动鼠标时画出轨迹
def motion(event):
    mouse_moves.append((event.x, event.y))
    canvas.create_line(mouse_moves, width=2)


# 响应鼠标事件
canvas.bind("<Button-1>", down)
canvas.bind("<B1-Motion>", motion)

# 创建右侧窗口
right_frame = tk.Canvas(root, width=720, height=450)
right_frame.pack(side="right", fill="both", expand=True)
# #* 分割线
# separator = tk.Frame(root, width=2, bg="black")
# separator.place(relx=0.5, rely=0, relheight=2, anchor="w")

screen = t.TurtleScreen(right_frame)
screen.bgcolor("white")

turtle = t.RawTurtle(screen)
turtle.pencolor("red")
turtle.pensize(2)

w = root.winfo_width()
h = root.winfo_height()
t_h = screen.window_height()
t_w = screen.window_width()

app = Turtle(root, turtle)
# app = App(left_frame)
# 运行主窗口
root.mainloop()
