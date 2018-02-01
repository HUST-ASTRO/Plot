# -*- coding: utf-8 -*-
# @Time    : 18-2-1 下午2:36
# @Author  : YuLiu
# @Email   : 335992260@qq.com
# @File    : CelestialSphere.py
# @Software: PyCharm


class CelestialSphere:
    def __init__(self, x, y, xerr=None, yerr=None, err=None, frame='icrs', unit=None):
        self.x = x
        self.y = y
        self.xerr = xerr
        self.yerr = yerr
        self.err = err
        self.frame = frame
        self.unit = unit

    def
