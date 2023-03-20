#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   draw_func.py
@Time    :   2023/03/16 22:15:59
@Author  :   Serein
@Version :   1.0
@Contact :   serein7z@163.com
@License :   (C)Copyright 2022-2023, USTB_MedicalAI
@Desc    :   {draw_func}
'''
import math


def view_line(canvas, mouse):
    canvas.create_line(mouse.moves, width=2)


def view_straight(canvas, mouse):
    start_x, start_y, end_x, end_y, _, _ = circle_pos(mouse)
    canvas.delete('view_line')
    canvas.create_line(start_x, start_y, end_x, end_y, width=2, tag='view_line')


def view_circle(canvas, mouse):
    start_x, start_y, new_end_x, new_end_y = circle_end_pos(mouse)
    canvas.delete('oval')
    canvas.create_oval(start_x, start_y, new_end_x, new_end_y, width=2, tag='oval')


def view_Rect(canvas, mouse):
    start_x, start_y, end_x, end_y, _, _ = circle_pos(mouse)
    canvas.delete('Rect')
    canvas.create_rectangle(start_x, start_y, end_x, end_y, width=2, tag='Rect')


def turtle_line(event, t, mouse):
    t.up()
    for x, y in mouse.moves:
        t.goto(x, y)
        t.down()
    mouse.moves.clear()


def turtle_straight(canvas, t, mouse):
    start_x, start_y, end_x, end_y, _, _ = circle_pos(mouse)
    canvas.create_line(start_x, start_y, end_x, end_y, width=2, tag='line_confirm')
    angle = math.atan((end_y - start_y) / (end_x - start_x)) * 180 / math.pi
    # if angle<0:
    #     angle = 180 + angle
    # elif angle >360:
    # angle = angle - 360
    # print(angle)
    if end_x - start_x < 0:
        angle = angle + 180
    print(angle)
    t.up()
    t.goto(start_x, start_y)
    t.down()
    t.seth(angle)
    t.forward(math.sqrt((end_x - start_x)**2 + (end_y - start_y)**2))

    mouse.moves.clear()


def turtle_circle(event, canvas, t, mouse):
    start_x, start_y, new_end_x, new_end_y = circle_end_pos(mouse)
    center_x = (start_x + new_end_x) / 2
    r = (new_end_y - start_y) / 2
    canvas.create_oval(start_x, start_y, new_end_x, new_end_y, width=2, tag='confirm')
    # if is_circle(mouse):
    t.up()
    t.goto(center_x, start_y)
    t.down()
    t.circle(r)
    # else:
    # oval(t, mouse)
    mouse.moves.clear()


def turtle_rect(event, canvas, t, mouse):
    start_x, start_y, end_x, end_y, _, _ = circle_pos(mouse)
    canvas.create_rectangle(start_x, start_y, end_x, end_y, width=2, tag='rec_confirm')
    h, w = end_y - start_y, end_x - start_x
    t.up()
    t.seth(0)
    t.goto(start_x, start_y)
    t.down()
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    mouse.moves.clear()


def circle_pos(mouse):
    start_x, start_y = mouse.moves[0]
    end_x, end_y = mouse.moves[-1]
    center_x = (start_x + end_x) / 2
    center_y = (start_y + end_y) / 2
    return start_x, start_y, end_x, end_y, center_x, center_y


def circle_end_pos(mouse):
    start_x, start_y = mouse.moves[0]
    end_x, end_y = mouse.moves[-1]
    length_1 = end_x - start_x
    length_2 = end_y - start_y
    circle_edge = length_1 if length_1 > length_2 else length_2
    if end_x > start_x and end_y < start_y:
        new_end_x = start_x + circle_edge
        new_end_y = start_y - circle_edge
    elif end_x < start_x and end_y > start_y:
        new_end_x = start_x - circle_edge
        new_end_y = start_y + circle_edge
    else:
        new_end_x = start_x + circle_edge
        new_end_y = start_y + circle_edge
    return start_x, start_y, new_end_x, new_end_y


def is_circle(mouse):
    start_x, start_y, end_x, end_y, center_x, center_y = circle_pos(mouse)
    if end_x - start_x == end_y - start_y:
        return True
    return False


def oval(t, mouse):
    start_x, start_y, end_x, end_y, center_x, center_y = circle_pos(mouse)
    oval_top_x = center_x - start_x
    oval_top_y = center_y - start_y
    t.up()
    t.goto(oval_top_x, oval_top_y)
    t.down()
    t.speed(0)

    for i in range(120):
        t.rt(3)
        t.fd(1)


def angle(start_x, start_y, end_x, end_y):
    angle = math.atan2(end_y - start_y, end_x - start_x)
    return angle