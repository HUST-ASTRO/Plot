# -*- coding: utf-8 -*-
# @Time    : 18-2-26 上午10:25
# @Author  : YuLiu
# @Email   : 335992260@qq.com
# @File    : KMeans.py
# @Software: PyCharm

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


class InputData:
    def __init__(self, data, scaled=False):

        # Scaled data(standard normal)
        if scaled:
            scaler = StandardScaler()
            data = scaler.fit_transform(data)

        self.data = data

    def score(self, n=range(2, 7)):
        km = []
        for n_clusters in n:
            km[n_clusters - 2] = KMeans(n_clusters=n_clusters).fit(data)


# class KMeansVisual:
#     def __init__(self, data, n_clusters, method, scaled=False):
#
#         # Scaled data
#         if scaled == True:
#             scaler = StandardScaler()
#             data = scaler.fit_transform(data)
#
#         km = KMeans(n_clusters=n_clusters).fit(data)
#
#         self._method_choices = {'scatter': self._scatter,
#                                 'color': self._color}
#
#         # simple test to validate method
#         if method in self._method_choices.keys():
#             self.method = method
#         else:
#             raise ValueError("Invalid Value for method: {0}".format(method))
#
#         self._method_choices[self.method]()
#
#     def _scatter(self):
#         print()
#
#     def _color(self):
#         print()


if __name__ == '__main__':
    filename = u'/home/hust/Desktop/Myproject/astroML/KMeans/data/Table_new.csv'
    Table = pd.read_csv(filename, usecols=['offset', 'T90']).dropna()
    a = InputData(Table, scaled=True)
    print(a.data)
