#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2023/03/22 10:39:25
@Author  :   Serein
@Version :   1.0
@Contact :   serein7z@163.com
@License :   (C)Copyright 2022-2023, USTB_MedicalAI
@Desc    :   {Statistics the number of lines of code in the project.}
'''
import os
import re
import pandas as pd


def one_comments(line):
    if re.match(r'^\s*#', line):
        return True
    return False


def multi_comments(line):
    if re.match(r"^\s*'''", line):
        return True
    return False


def match_def(line):
    if re.match(r'^\s*def', line):
        return True
    return False


def statistics_line(lines, content, sentence_list):
    result = {
        'total_line': 0,
        'one_comment': 0,
        'multi_comment': 0,
        'total_comment': 0,
        'blank': 0,
        'work_line': 0,
        'line_length': 0,
        'mean_length': 0,
        'max_indent': 0,
        'if_num': 0,
        'for_num': 0,
        'while_num': 0,
        'try_num': 0,
        'except_num': 0,
        'func_num:': 0,
        'mean_func_line': 0,
        'variable_num': 0,
        'variable_len': 0,
        'mean_variable': 0,
    }
    variable_name_dict = {}
    result['total_line'] = len(lines)
    comment_index = []
    func_index = []
    max_indent = 0
    variable_length = 0
    for index, line in enumerate(lines):
        comment_flag = False
        func_flag = False
        #* before find the end of comment block, keep the comment_flag True
        if len(comment_index) % 2 != 0:
            comment_flag = True

        #* before find the end of function block, keep the func_flag True
        if len(func_index) % 2 and len(func_index):
            func_flag = True

        #* get total line length
        result['line_length'] += len(line)

        #* find comment starts with #
        if one_comments(line):
            result['one_comment'] += 1
            comment_flag = True

        #* find comment starts or ends with '''
        elif multi_comments(line):
            comment_index.append(index)
            comment_flag = True

        #* find blank line
        elif re.match(r'^\s*$', line):
            result['blank'] += 1

        #* find max indent
        indent_match = re.match(r'^(\s*)\S', line)
        if indent_match:
            indent = indent_match.group(1)
            max_indent = max(max_indent, len(indent) // 4)
        #* find if, for, while, try, except
        for s in sentence_list:
            if re.match(rf'^\s*{s}', line):
                result[f'{s}_num'] += 1

    #* find function block
    pattern = r'\n?[ ]*def\s+\w+\(.*?\):(?:\n[ ]+.+)+'
    matches = re.findall(pattern, content)

    #* count func num
    result['func_num:'] = len(matches)
    func_line = 0
    a = 2
    for func in matches:
        func_line += func.count('\n')
        variable_dict = {}
        this_name = []
        func_name = re.match(r'\s*def\s+(\w+).*:', func).group(1)

        #* find all assignment sentence
        let_sentence = re.findall(r'\s*\#?\s*(?:\w+,?\s)+=\s+.*[^\)]', func)
        if let_sentence:
            for sentence in let_sentence:
                if "#" in sentence:
                    continue
                variable = sentence.strip().replace(' ', '').split('=')[0].split(',')
                for v in variable:
                    if v not in variable_dict:
                        variable_dict[v] = 1
                        this_name.append(v)
                        result['variable_len'] += len(v)
                        result['variable_num'] += 1
                variable_name_dict[func_name] = this_name

    #* count mean of function line
    result['mean_func_line'] = int(func_line / result['func_num:'])

    #* count mean of variable length
    result['mean_variable'] = int(result['variable_len'] / result['variable_num'])

    #*i
    for i in range(0, len(comment_index), 2):
        result['multi_comment'] += comment_index[i + 1] - comment_index[i] + 1
    result['work_line'] = result['total_line'] - result['one_comment'] - result['multi_comment'] - result['blank']

    result['mean_length'] = int(result['line_length'] / result['work_line'])
    result['total_comment'] = result['one_comment'] + result['multi_comment']
    result['max_indent'] = max_indent

    return result, variable_name_dict


if __name__ == '__main__':
    file_path = './target_py.py'
    sentence_list = ['if', 'for', 'while', 'try', 'except']
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        f.seek(0)
        content = f.read()

        result, v_name = statistics_line(lines, content, sentence_list)
        # for key, value in result.items():
        #     print(key, value)

        #* 写入txt
        txt_dict = {
            '总行数': result['total_line'],
            '注释行数': result['total_comment'],
            '空行数': result['blank'],
            '有效代码行数': result['work_line'],
            '代码行平均长度': result['mean_length'],
            '最大缩进层级': result['max_indent'],
            'if语句数': result['if_num'],
            'for语句数量': result['for_num'],
            'while语句数量': result['while_num'],
            'try语句数量': result['try_num'],
            'except语句数量': result['except_num'],
            '函数数量': result['func_num:'],
            '函数平均行数': result['mean_func_line'],
            '变量数': result['variable_num'],
            '变量名平均长度': result['mean_variable']
        }
        with open('result.txt', 'w', encoding='utf-8') as f:
            for key, value in txt_dict.items():
                f.write(f'{key}: {value}\r\n')
                print(f'{key}: {value}\r\n')
            for key, value in v_name.items():
                f.write(f'\n函数{key}定义变量:\n')
                print(f'\n函数{key}定义变量:\n')
                if value == []:
                    f.write('    无\n')
                    print(f'    无\n')
                for name in value:
                    if name:
                        f.write(f'    {name}\n')
                        print(f'    {name}\n')