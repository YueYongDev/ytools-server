# coding=utf-8
'''
  Created by lyy on 2019-04-29
'''
from secure import BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY
from app.utils.common_utils import get_file_content

__author__ = 'lyy'

from aip import AipImageClassify

APP_ID = BAIDU_APP_ID
API_KEY = BAIDU_API_KEY
SECRET_KEY = BAIDU_SECRET_KEY

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)


# 识别动物
def animals_classify(img):
    image = get_file_content(img)

    """ 调用动物识别 """
    res = client.animalDetect(image)
    return res


# 识别植物
def plant_classify(img):
    image = get_file_content(img)

    """ 调用植物识别 """
    res = client.plantDetect(image)
    return res


# 识别车辆
def car_classify(img):
    image = get_file_content(img)

    """ 调用车辆识别 """
    res = client.carDetect(image)
    return res


if __name__ == '__main__':
    res = animals_classify('temp/animal.jpg')
    print(res)
