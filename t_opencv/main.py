# -*- coding: utf-8 -*-
"""
@author 仔仔
@date 2024-03-25 23:34:45
@describe TODO
"""
import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np


def main():
    t2()


def t1():
    filename = "./images/test.png"
    print("opencv version:", cv2.getVersionString())

    # imread 读取图像
    image_unchanged = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    image_grayscale = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    image_color = cv2.imread(filename, cv2.IMREAD_COLOR)

    # imshow 显示图像
    cv2.imshow('unchanged', image_unchanged)
    cv2.imshow('grayscale', image_grayscale)
    cv2.imshow('color', image_color)

    # 永远暂停程序直到键击任意键
    cv2.waitKey(0)
    # 销毁所有窗口
    cv2.destroyAllWindows()


def t2():
    filename = "./images/test.png"
    print("opencv version:", cv2.getVersionString())

    # imread 读取图像
    image_unchanged = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    img_add_text = cv2_chinese_text(image_unchanged, "你好 世界", 10, 10)
    cv2.imshow('图片添加文字', img_add_text)
    # 永远暂停程序直到键击任意键
    cv2.waitKey(0)
    # 销毁所有窗口
    cv2.destroyAllWindows()

def cv2_chinese_text(img, text, left, top, text_color=(0, 255, 255)):
    text_size = 25
    # 判断是否OpenCV图片类型
    if isinstance(img, np.ndarray):
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 字体的格式
    font_style = ImageFont.truetype("simfang.ttf",
                                    text_size, encoding="utf-8")
    # 绘制文本
    draw.text((left, top), text, text_color, font=font_style)
    # 转换回OpenCV格式
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)


if __name__ == '__main__':
    main()
