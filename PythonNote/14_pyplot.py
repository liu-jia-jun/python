# 数据可视化，数据分析

import matplotlib.pyplot as plt

import numpy as np

# 绘图第一步，创建画布
plt.figure(figsize=(4,4))

# 第二布，绘图

num = np.arange(10)
plt.plot(np.sin(num))
plt.plot(np.cos(num))

plt.legend(["sin","cos"])

# plt.savefig("aaa.png")

plt.show()

num = numpy.arange(0,np.pi*2,0.01)

ax1 = p.add_subplot(3,1,3)

plt.plot(np.sin(num))

plt.plot(np.cos(num))

