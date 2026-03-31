import matplotlib.pyplot as plt
import numpy as np

def read_off_file(filename):
    with open(filename, 'r') as file:
        # 跳过注释行
        first_line = file.readline().strip()
        while first_line.startswith('#'):
            first_line = file.readline().strip()
        
        if 'OFF' not in first_line:
            raise ValueError("Not a valid OFF file")
        
        # 跳过可能的注释行，直到读取顶点和面的数量
        line = file.readline().strip()
        while line.startswith('#'):
            line = file.readline().strip()
        n_vertices, n_faces, _, _ = map(int, line.split(' '))
        
        # 读取顶点数据，跳过注释行
        vertices = []
        for _ in range(n_vertices):
            line = file.readline().strip()
            while line.startswith('#'):
                line = file.readline().strip()
            vertices.append(list(map(float, line.split(' '))))
        
        return np.array(vertices)

def plot_4d_data(data):
    if data.shape[1] < 4:
        raise ValueError("Data does not have 4 dimensions")
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    sc = ax.scatter(data[:,0], data[:,1], data[:,2], c=data[:,3], cmap='viridis')
    plt.colorbar(sc, label='4th Dimension')
    plt.show()

# 读取OFF文件并获取顶点数据
filename = '4d_shape.off'  # 替换为你的OFF文件路径
data = read_off_file(filename)

# 绘制四维数据
plot_4d_data(data)