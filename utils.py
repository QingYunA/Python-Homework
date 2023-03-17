#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   utils.py
@Time    :   2023/03/16 22:08:59
@Author  :   Serein
@Version :   1.0
@Contact :   serein7z@163.com
@License :   (C)Copyright 2022-2023, USTB_MedicalAI
@Desc    :   {utils}
'''
import turtle
import tkinter as tk
from draw_func import *


# 移动鼠标时画出轨迹
def preview_func(event, canvas, mouse):
    mouse.moves.append((event.x, event.y))
    if mouse.status == 'draw':
        view_line(canvas, mouse)
    elif mouse.status == 'circle':
        view_circle(canvas, mouse)
    elif mouse.status == 'rect':
        view_Rect(canvas, mouse)


def draw_func(event, t, canvas, mouse):
    if mouse.status == 'draw':
        turtle_line(event, t, mouse)
    if mouse.status == 'circle':
        turtle_circle(event, canvas, t, mouse)
    if mouse.status == 'rect':
        turtle_rect(event, canvas, t, mouse)


def normal_status(mouse):
    mouse.normal()


def circle_status(mouse):
    mouse.circle()


def Rect_status(mouse):
    mouse.Rect()


def clear(canvas, turtle_canvas, mouse):
    print('clear')
    canvas.delete('all')
    turtle_canvas.delete('all')