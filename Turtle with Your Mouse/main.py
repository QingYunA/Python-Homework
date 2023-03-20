#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2023/03/15 10:45:49
@Author  :   Serein
@Version :   1.0
@Contact :   serein7z@163.com
@License :   (C)Copyright 2022-2023, USTB_MedicalAI
@Desc    :   {turtle with your mouse! guided by chatgpt}
'''
import tkinter as tk
from utils import *
from init import *

if __name__ == '__main__':
    mouse = Mouse()
    #* 初始化窗口
    root, canvas, turtle_canvas = init(mouse)

    #* 初始化turtle
    t = init_turtle(turtle_canvas, speed=10)

    #* 响应鼠标事件
    # canvas.bind("<Button-1>", lambda event: B1_click(event, mouse_moves))
    canvas.bind("<B1-Motion>", lambda event: preview_func(event, canvas, mouse))
    canvas.bind("<ButtonRelease-1>", lambda event: draw_func(event, t, canvas, mouse))

    root.mainloop()
