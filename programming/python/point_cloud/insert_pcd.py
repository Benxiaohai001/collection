import os
import subprocess
import json

def get_pcd_files(directory):
    """
    获取指定目录下所有后缀为.pcd的文件
    :param directory: 目录路径
    :return: 后缀为.pcd的文件列表
    """
    pcd_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".pcd"):
                pcd_files.append(os.path.join(root, file))
    return pcd_files

def upload_pcd_files(pcd_files):
    """
    为每个PCD文件执行curl命令上传
    :param pcd_files: PCD文件列表
    """
    for pcd_file in pcd_files:
        pcd_name = os.path.basename(pcd_file)
        curl_command = f'curl -i -u "root:" -XPOST "http://127.0.0.1:9902/api/v1/upload?db=pcd&file={pcd_name}" -T "{pcd_file}"'
        result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)
        if "200 OK" in result.stdout:
            print(f"{pcd_name} 上传成功。")
        else:
            print(f"{pcd_name} 上传失败。")
        compare_points(pcd_file)

def get_points_number(pcd_file):
    """
    从PCD文件中获取POINTS后面的数字
    :param pcd_file: PCD文件路径
    :return: POINTS后面的数字
    """
    with open(pcd_file, 'r') as file:
        for line in file:
            if line.startswith('POINTS'):
                return int(line.split()[1])
    return None

def execute_sql_query(pcd_file):
    """
    执行SQL查询命令，返回查询到的点的数量
    :param pcd_file: 包含路径的PCD文件名
    :return: 查询到的点的数量
    """
    pcd_name_with_extension = os.path.basename(pcd_file)
    pcd_name, _ = os.path.splitext(pcd_name_with_extension)  # 移除文件后缀
    curl_command = f'curl -s -u "root:" -XPOST "http://127.0.0.1:9902/api/v1/sql?db=pcd" -d "select count(*) from {pcd_name}"'
    result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)
    try:
        # 假设返回的是JSON格式，且包含查询结果
        data = json.loads(result.stdout)
        return data['rows'][0][0]  # 根据实际返回的数据结构调整
    except json.JSONDecodeError:
        return None

def compare_points(pcd_file):
    """
    比较get_points_number和execute_sql_query获得的值
    :param pcd_file: PCD文件路径
    """
    points_number = get_points_number(pcd_file)
    query_result = execute_sql_query(pcd_file)

    if points_number == query_result:
        print("成功: 两个函数返回的值相同。")
    else:
        print(f"失败: get_points_number返回{points_number}, execute_sql_query返回{query_result}。")


# 使用示例
directory_path = os.getcwd()
pcd_files = get_pcd_files(directory_path)
upload_pcd_files(pcd_files)
