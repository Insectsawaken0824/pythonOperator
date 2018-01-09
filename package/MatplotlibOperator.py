# -*- coding:utf-8 -*-

import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import math

if __name__ == "__main__":
    # 5.绘图
    # 5.1 绘制正态分布概率密度函数
    mpl.rcParams['font.sans-serif'] = [u'SimHei']  # FangSong/黑体 FangSong/KaiTi
    mpl.rcParams['axes.unicode_minus'] = False
    mu = 0
    sigma = 1
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 51)
    y = np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma)
    print x.shape
    print 'x = \n', x
    print y.shape
    print 'y = \n', y
    plt.figure(facecolor='w')
    # linewidth 线宽  mec 描边
    plt.plot(x, y, 'ro-', linewidth=2, mec='k')
    # plt.plot(x, y, 'r-', x, y, 'go', linewidth=2, markersize=8)
    plt.xlabel('X', fontsize=15)
    plt.ylabel('Y', fontsize=15)
    plt.title(u'高斯分布函数', fontsize=18)    #
    # linestyle 可设置成虚线
    plt.grid(True, linestyle="--")
    plt.show()