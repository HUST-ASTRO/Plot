# -*- coding: utf-8 -*-
# @Time    : 18-2-26 上午10:25
# @Author  : YuLiu
# @Email   : 335992260@qq.com
# @File    : KMeans.py
# @Software: PyCharm


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


class InputData:
    def __init__(self, data, scaled=False):
        self._method_choices = {'scatter': self._scatter,
                                'color': self._color}
        self.method = None
        self.label = None
        self.centroids = None
        self.km = None

        # Scaled data(standard normal)
        if scaled:
            scaler = StandardScaler()
            data = scaler.fit_transform(data)

        self.data = data

    def silhouette(self, n=range(2, 7)):
        score = []
        for n_clusters in n:
            km = KMeans(n_clusters=n_clusters).fit(self.data)
            score.append(metrics.silhouette_score(self.data, km.labels_))

        plt.title('Silhouette Coefficient')
        plt.xlabel('n_clusters')
        plt.ylabel('score')
        plt.xticks(n)
        plt.plot(n, score, 'o-')
        plt.show()

        return score

    def clustering(self, n_clusters):
        km = KMeans(n_clusters=n_clusters).fit(self.data)

        self.km = km
        self.label = km.labels_
        self.centroids = km.cluster_centers_

    def plot(self, method):
        # simple test to validate method
        if method in self._method_choices.keys():
            self.method = method
        else:
            raise ValueError("Invalid Value for method: {0}".format(method))

        self._method_choices[self.method]()

    def _scatter(self):
        numSamples = len(self.data)
        labels = self.label
        mark = ['r.', 'b.']

        # 画出所有样例点 属于同一分类的绘制同样的颜色
        for i in range(numSamples):
            # markIndex = int(clusterAssment[i, 0])
            plt.plot(self.data[i][0], self.data[i][1], mark[labels[i]])  # mark[markIndex])
        centroids = self.centroids
        for i in range(2):
            plt.plot(centroids[i][0], centroids[i][1], 'k+', markersize=18)
            # print centroids[i, 0], centroids[i, 1]
        plt.title('offset-T90', size=14)
        plt.xlabel('T90', size=14)
        plt.ylabel('offset', size=14)

    def _color(self):
        # Step size of the mesh. Decrease to increase the quality of the VQ.
        h = .01  # point in the mesh [x_min, x_max]x[y_min, y_max].

        # Plot the decision boundary. For that, we will assign a color to each
        x_min, x_max = self.data['T90'].min() - 0.2, self.data['T90'].max() + 0.2
        y_min, y_max = self.data['offset'].min() - 0.2, self.data['offset'].max() + 0.2
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

        # Obtain labels for each point in mesh. Use last trained model.
        Z = self.km.predict(np.c_[xx.ravel(), yy.ravel()])

        # Put the result into a color plot
        Z = Z.reshape(xx.shape)

        plt.imshow(Z, interpolation='nearest',
                   extent=(xx.min(), xx.max(), yy.min(), yy.max()),
                   cmap=plt.get_cmap('bwr'),
                   aspect='auto', origin='lower')

        self.data['scaled_cluster'] = self.label
        centers = self.data.groupby('scaled_cluster').mean().reset_index()

        # score = metrics.silhouette_score(data, Table.scaled_cluster)
        # print(score)

        # pd.scatter_matrix(Table, c=colours[Table.scaled_cluster], alpha=1, figsize=(10, 10), s=100)
        plt.scatter(self.data['T90'], self.data['offset'], c='k')
        plt.scatter(centers.T90, centers.offset, linewidths=3, marker='+', s=300, c='w')
        # plt.title('offset-T90')
        plt.xlabel('T90')
        plt.ylabel('offset')


if __name__ == '__main__':
    filename = u'/home/hust/Desktop/Myproject/astroML/KMeans/data/Table_new.csv'
    Table = pd.read_csv(filename, usecols=['offset', 'T90']).dropna()
    a = InputData(Table)
