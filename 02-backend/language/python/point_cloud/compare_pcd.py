# Import libraries
import base64
import numpy as np
import pypcd4
import os
import glob
import urllib.request

# Definitions

## CnosDB API Constants
api_sql = 'http://127.0.0.1:8902/api/v1/sql'
api_write_point_cloud = 'http://127.0.0.1:8902/api/v1/point_cloud/write'
api_dump_point_cloud = 'http://127.0.0.1:8902/api/v1/point_cloud/dump'
api_delete_point_cloud = 'http://127.0.0.1:8902/api/v1/point_cloud/delete'
http_headers = {
    'Authorization': 'Basic ' + base64.b64encode(bytes('root:', 'utf-8')).decode('utf-8')
}
database_name_point_cloud = 'pcd'

## Test Constants

base_dir = os.getcwd()
test_source_dir = base_dir + '/test_source'
test_target_dir = base_dir + '/test_target'

## Variables & Functions

sql_create_point_cloud_database = 'CREATE DATABASE IF NOT EXISTS %s WITH point_cloud true;' % database_name_point_cloud

def mkdir_ignore_error(path):
    try:
        os.mkdir(path)
    except:
        pass

mkdir_ignore_error(base_dir)
print("Base directory created:", base_dir)
mkdir_ignore_error(test_source_dir)
print("Source directory created:", test_source_dir)
mkdir_ignore_error(test_target_dir)
print("Target directory created:", test_target_dir)
test_file_ids_and_names = [] # [(point_cloud_id, file_name)]

pcd_files = glob.glob(os.path.join(test_source_dir, '*.pcd'))

# 获取文件名（不包括文件后缀）、文件名带后缀（不包括路径）
for file_path in pcd_files:
    file_name_without_extension = os.path.splitext(os.path.basename(file_path))[0]
    file_name_with_extension = os.path.basename(file_path)
    test_file_ids_and_names.append((file_name_without_extension, file_name_with_extension))

print(f"test_file_ids_and_names is:{test_file_ids_and_names}")


def request_api_v1_sql(sql):
    url = api_sql + '?db=public'
    req = urllib.request.Request(url, method='POST', headers=http_headers, data=sql.encode('utf-8'))
    resp = urllib.request.urlopen(req)
    if resp.status != 200:
        raise Exception('Failed to execute SQL: %s' % sql)
    return resp.read().decode('utf-8')

request_api_v1_sql(sql_create_point_cloud_database)
print("Database created:", database_name_point_cloud)

def request_api_v1_point_cloud_write(id, in_path):
    url = '%s?db=%s&id=%s&fmt=%s' % (api_write_point_cloud, database_name_point_cloud, id, 'pcd')
    print("Uploading point cloud file:", url)
    file_bytes = open(in_path, 'rb').read()
    req = urllib.request.Request(url, method='POST', headers=http_headers, data=file_bytes)
    resp = urllib.request.urlopen(req)
    if resp.status != 200:
        raise Exception('Failed to write point cloud file: id=%s, in_path=%s' % (id, in_path))
    return resp.read().decode('utf-8')

def request_api_v1_point_cloud_dump(id, out_path):
    url = '%s?db=%s&id=%s' % (api_dump_point_cloud, database_name_point_cloud, id)
    print("Downloading point cloud file:", url)
    req = urllib.request.Request(url, method='GET', headers=http_headers)
    resp = urllib.request.urlopen(req)
    if resp.status != 200:
        raise Exception('Failed to dump point cloud file: id=%s, out_path=%s' % (id, out_path))
    file_bytes = resp.read()
    open(out_path, 'wb').write(file_bytes)

def request_api_v1_point_cloud_delete(id):
    url = '%s?db=%s&id=%s' % (api_delete_point_cloud, database_name_point_cloud, id)
    print("Deleting point cloud file:", url)
    req = urllib.request.Request(url, method='POST', headers=http_headers)
    resp = urllib.request.urlopen(req)
    if resp.status != 200:
        raise Exception('Failed to delete point cloud file: id=%s' % id)
    file_bytes = resp.read()
    return resp.read().decode('utf-8')

# Write to CnosDB
def write_data_to_cnosdb(test_file_ids_and_names):
    for (pcd_file_id, pcd_file_name) in test_file_ids_and_names:
        test_source_file_path = '%s/%s' % (test_source_dir, pcd_file_name)
        request_api_v1_point_cloud_write(pcd_file_id, test_source_file_path)
        print('Uploaded source file:', test_source_file_path)

# Dump from CnosDB
def dump_from_cnosdb(test_file_ids_and_names):
    for (pcd_file_id, pcd_file_name) in test_file_ids_and_names:
        test_target_file_path = '%s/%s' % (test_target_dir, pcd_file_name)
        request_api_v1_point_cloud_dump(pcd_file_id, test_target_file_path)
        print('Downloaded target file:', test_target_file_path)

# Compare the original and dumped files
def compare_original_dump_file(test_file_ids_and_names):
    for (pcd_file_id, pcd_file_name) in test_file_ids_and_names:
        test_source_file_path = '%s/%s' % (test_source_dir, pcd_file_name)
        test_target_file_path = '%s/%s' % (test_target_dir, pcd_file_name)
        print('Comparing source and target files:', test_source_file_path, test_target_file_path)
        source_file = pypcd4.PointCloud.from_path(test_source_file_path)
        target_file = pypcd4.PointCloud.from_path(test_target_file_path)
        if source_file.metadata == target_file.metadata:
            print('Meta equals? True')
        else:
            print('Meta equals? False')
            source_metadata = source_file.metadata
            target_metadata = target_file.metadata
            print(f"source_metadata: {source_metadata}")
            print(f"target_metadata: {target_metadata}")
        # print(f"source_file.pc_data.dtype : {source_file.pc_data.dtype}")
        source_file_bak = source_file.pc_data
        target_file_bak = target_file.pc_data
        for field in source_file.pc_data.dtype.names:
            source_file_bak[field] = np.nan_to_num(source_file.pc_data[field], nan=0)
        for field in target_file.pc_data.dtype.names:
            target_file_bak[field] = np.nan_to_num(target_file.pc_data[field], nan=0)
        if np.array_equal(source_file_bak, target_file_bak):
            print('Data equals? True')
        else:
            nan = np.nan_to_num(source_file.pc_data, nan=0)
            print(f"target_file_bak: {target_file_bak}")
            print(f"source_file_bak: {source_file_bak}")
# Clear CnosDB
def clear_cnosdb(test_file_ids_and_names):
    for (pcd_file_id, pcd_file_name) in test_file_ids_and_names:
        request_api_v1_point_cloud_delete(pcd_file_id)
        print('Deleted file:', pcd_file_name)

write_data_to_cnosdb(test_file_ids_and_names)
dump_from_cnosdb(test_file_ids_and_names)
compare_original_dump_file(test_file_ids_and_names)
clear_cnosdb(test_file_ids_and_names)