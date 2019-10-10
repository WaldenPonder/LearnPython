# from tkinter import *

# root = Tk()
# root.geometry('1000x800+500+100')
# root.title('BSF')
# root.mainloop()

import numpy as np

import matplotlib.pyplot as plt
import random

# 数据量。
SIZE = 13
# 纵轴数据。np.linspace 返回一个一维数组，SIZE指定数组长度。                                
# 数组最小值是-6，最大值是6。所有元素间隔相等。整个数组是
# 个等差数列。
Y = np.linspace(-6, 6, SIZE)
# 横轴数据。 
X = np.linspace(-2, 3, SIZE)

fig = plt.figure()
# 画图区域分成1行1列。选择第一块区域。
ax1 = fig.add_subplot(1, 1, 1)
# 标题
ax1.set_title("SCATTER PLOT")
# 让散点图的数据更加随机。
random_x = []
random_y = []
for i in range(SIZE):
    random_x.append(X[i] + random.uniform(-1, 1))
for i in range(SIZE):
    random_y.append(Y[i] + random.uniform(-1, 1))
RANDOM_X = np.array(random_x)  # 散点图的横轴。
RANDOM_Y = np.array(random_y)  # 散点图的纵轴。

# 画散点图。
ax1.scatter(RANDOM_X, RANDOM_Y)
# 横轴名称。
ax1.set_xlabel("x")
# 纵轴名称。
ax1.set_ylabel("y")

# 直线图
# ax1.plot(X, Y)
plt.show()