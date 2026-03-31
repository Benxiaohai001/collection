import numpy as np
from stl import mesh
import requests


base_url = "http://127.0.0.1:8902"

def generate_random_stl(file_path, num_faces):
    """
    随机生成三角形面数据并写入 .stl 文件
    """
    # 每个面有三个顶点，每个顶点有三个坐标值（x, y, z）
    data = np.zeros(num_faces, dtype=mesh.Mesh.dtype)
    
    for i in range(num_faces):
        for j in range(3):
            data['vectors'][i][j] = np.random.rand(3)
    
    # 创建 mesh 对象
    random_mesh = mesh.Mesh(data)
    
    # 保存为 .stl 文件
    random_mesh.save(file_path)
    print(f'STL file generated: {file_path}')

def upload_stl_to_database(file_path, url):
    """
    将 .stl 文件通过接口上传到数据库
    """
    
    with open(file_path, 'rb') as file:
        files = {'file': (file_path, file, 'application/sla')}
        response = requests.post(url, files=files)
        
        if response.status_code == 200:
            print('File uploaded successfully')
        else:
            print(f'Failed to upload file: {response.status_code}')
            print(response.text)

def main():
    file_path = 'random_sample.stl'
    num_faces = 100  # 三角形面数量
    
    generate_random_stl(file_path, num_faces)

if __name__ == "__main__":
    main()