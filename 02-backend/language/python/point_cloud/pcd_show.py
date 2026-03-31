import pcl
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 读取PCD文件
pcd = pcl.load('~/Downloads/slam.pcd')

# 将点云数据转换为numpy数组
points = np.array(pcd.to_array())

# 创建一个3D绘图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制点云数据
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=points[:, 2], cmap='viridis', s=1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
