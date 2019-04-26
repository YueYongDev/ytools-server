# coding=utf-8
'''
  Created by lyy on 2019-04-19
'''

__author__ = 'lyy'

from flask import Blueprint

# 定义一个蓝图
img = Blueprint('img', __name__)

from app.api.v1.img import ph_logo, stylize


@img.route('/')
def say_hello():
    return '这里是图片处理类的接口'