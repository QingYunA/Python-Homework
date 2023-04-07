#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2023/04/07 09:53:37
@Author  :   Serein
@Version :   1.0
@Contact :   serein7z@163.com
@License :   (C)Copyright 2022-2023, USTB_MedicalAI
@Desc    :   {}
'''
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileReader
from utils import pdf_to_image
from pathlib import Path
from reportlab.lib.colors import black
from tqdm import tqdm
import shutil
from PIL import Image
# 注册字体
song = "simsun"
pdfmetrics.registerFont(TTFont(song, "simsun.ttc"))
PAGE_HEIGHT = A4[1]
PAGE_WIDTH = A4[0]


def read_pdf(pdf_path):
    pdf_file = open(pdf_path, 'rb')
    reader = PdfFileReader(pdf_file)
    num_pages = reader.getNumPages()

    return reader, num_pages


def get_pos():
    img_pos = []
    line_pos = []
    for i in range(4):
        img_pos.append([0.05 * PAGE_WIDTH, (0.760 - i * 0.24) * PAGE_HEIGHT])
    for i in range(16):
        line_pos.append([0.55 * PAGE_WIDTH, (0.90 - i * 0.05) * PAGE_HEIGHT])
    return img_pos, line_pos


def main():
    pdf_path = './CH07.pdf'
    image_path = './images'
    bar_code_path = './bar_code.png'
    output_path = './notebook.pdf'
    line_width = 1

    pdf_to_image(pdf_path, output_folder=image_path, image_format='jpg', dpi=600)
    c = canvas.Canvas(output_path, pagesize=A4)
    c.setStrokeColor(black)
    c.setLineWidth(line_width)
    images_path = sorted(Path(image_path).glob('*'))
    num_images = len(images_path)

    img_pos, line_pos = get_pos()
    for index, i in tqdm(enumerate(images_path), total=num_images, desc='Generating PDF'):
        img = Image.open(i)
        c.drawInlineImage(img,
                          img_pos[index % 4][0],
                          img_pos[index % 4][1],
                          width=0.45 * PAGE_WIDTH,
                          height=0.25 * PAGE_HEIGHT)
        #* image complete
        if (index + 1) % 4 == 0:
            #* draw line
            c.drawInlineImage(bar_code_path,
                              0.84 * PAGE_WIDTH,
                              0.94 * PAGE_HEIGHT,
                              width=0.15 * PAGE_WIDTH,
                              height=0.05 * PAGE_HEIGHT)
            for i in line_pos:
                c.line(i[0], i[1], i[0] + 0.4 * PAGE_WIDTH, i[1])
            c.showPage()

    c.save()
    shutil.rmtree(image_path)


if __name__ == '__main__':
    main()
