#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2023/03/20 10:51:55
@Author  :   Serein
@Version :   1.0
@Contact :   serein7z@163.com
@License :   (C)Copyright 2022-2023, USTB_MedicalAI
@Desc    :   {draw mathematical with Turtle}
'''
import turtle
from init import *
from random import sample, choice
import random


def init_turtle(speed, pensize=3, hide=True):
    screen = turtle.Screen()
    screen.title("Mathematical Calculation")
    screen.bgcolor("white")
    screen.tracer(0)
    t = turtle.Turtle()
    t.speed(speed)
    t.pensize(pensize)
    t.up()
    if hide:
        t.hideturtle()
    return t, screen


def sample():
    operation = choice(['+', '-', '×', '/'])
    num = random.sample(range(1, 100), 2)
    return num, operation


def check(num, operation):
    flag = False
    if operation == '+':
        answer = num[0] + num[1]
    elif operation == '-':
        answer = num[0] - num[1]
    elif operation == '×':
        answer = num[0] * num[1]
    elif operation == '/':
        answer = int(num[0] / num[1])

    if answer >= 0 and answer <= 99:
        flag = True
    if operation == '/':
        if num[0] % num[1] != 0:
            flag = False
    return answer, flag


def turtle_go(t, screen, first, line, column, corner_ratio=0.5, line_ratio=0.08, column_ratio=0.1):
    w_height = screen.window_height()
    w_width = screen.window_width()
    top_dis = w_height / 2
    bottom_dis = -w_height / 2
    left_dis = -w_width / 2
    right_dis = w_width / 2

    x = int(left_dis * (1 - corner_ratio) + column * column_ratio * w_width)
    y = int(top_dis * (1 - corner_ratio) - line * line_ratio * w_height)
    if first:
        t.goto(x - 50, y + 40)
        t.write(f'试题', font=("宋体", 15, "normal"), move=False, align="center")
        t.down()
        t.seth(0)
        t.fd(580)
        t.up()
    t.goto(x, y)


def turtle_go_answer(t,
                     screen,
                     first,
                     line,
                     column,
                     corner_ratio=0.5,
                     line_ratio=0.08,
                     column_ratio=0.1,
                     answer_ratio=0.4):
    w_height = screen.window_height()
    w_width = screen.window_width()
    top_dis = w_height / 2
    bottom_dis = -w_height / 2
    left_dis = -w_width / 2
    right_dis = w_width / 2

    x = int(left_dis * (1 - corner_ratio) + column * column_ratio * w_width)
    y = int(top_dis * (1 - corner_ratio) - line * line_ratio * w_height - answer_ratio * w_height)
    if first:
        t.goto(x - 50, y + 40)
        t.write(f'答案', font=("宋体", 15, "normal"), move=False, align="center")
        t.down()
        t.seth(0)
        t.fd(580)
        t.up()
    t.goto(x, y)


def rect(t, r):
    t.seth(0)
    t.down()
    t.fd(r)
    t.lt(90)
    t.fd(r)
    t.lt(90)
    t.fd(r)
    t.lt(90)
    t.fd(r)
    t.up()


def rect_with_text(t, r, answer):
    t.seth(0)
    t.down()
    t.fd(r / 2)
    t.up()
    pos = t.pos()
    t.write(f'{answer}', font=("宋体", 15, "normal"), move=False, align="center")
    t.goto(pos)
    t.seth(0)
    t.down()
    t.fd(r / 2)
    t.lt(90)
    t.fd(r)
    t.lt(90)
    t.fd(r)
    t.lt(90)
    pos = t.pos()
    t.fd(r)
    t.up()


if __name__ == '__main__':
    t, screen = init_turtle(speed=5, pensize=1, hide=False)  #* True False
    line = 5
    column = 3
    rect_length = 25
    first = True
    first_answer = True
    for i in range(line):
        for j in range(column):
            flag = False
            while (not flag):
                num, operation = sample()
                answer, flag = check(num, operation)

            #* 绘制题目
            turtle_go(t, screen, first, i, j, corner_ratio=0.3, line_ratio=0.08, column_ratio=0.2)
            first = False
            t.write(f'{str(num[0])} {operation} {str(num[1])} = ', font=("宋体", 15, "normal"), move=True, align="left")
            rect(t, r=rect_length)

            #* 绘制答案
            turtle_go_answer(t, screen, first_answer, i, j, corner_ratio=0.3, line_ratio=0.08, column_ratio=0.2)
            first_answer = False
            t.write(f'{str(num[0])} {operation} {str(num[1])} = ', font=("宋体", 15, "normal"), move=True, align="left")
            rect_with_text(t, r=rect_length, answer=answer)

    turtle.exitonclick()