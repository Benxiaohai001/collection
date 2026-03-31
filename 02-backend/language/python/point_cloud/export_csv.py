import requests
import json
from requests.auth import HTTPBasicAuth

url = "http://127.0.0.1:8902/api/v1/sql"
headers = {"Accept": "application/json"}
# get dbs list;
data = "show databases;"
response = requests.post(url, headers=headers, data=data, auth=HTTPBasicAuth('root', ''))
dbs = [db['database_name'] for db in json.loads(response.text) if db['database_name'] != "usage_schema"]
print("dbs is: {}", dbs);

# get tables list;
for db in dbs:
    url_table = url + "?db={}".format(db)
    data = "show tables;"
    # response = requests.post(url, headers=headers, data=data, auth=HTTP
    response = requests.post(url_table, headers=headers, data=data, auth=HTTPBasicAuth('root', ''))
    tables = [table['table_name'] for table in json.loads(response.text)]
    print("tables in db {} is: {}".format(db, tables))
    for table in tables:
        data = "copy into  'file:///tmp/data/{}/{}' from {} FILE_FORMAT = (TYPE = 'CSV', DELIMITER = ',');".format(db,table, table)
        response = requests.post(url_table, headers=headers, data=data, auth=HTTPBasicAuth('root', ''))
        print("data in table {} is: {}".format(table, response.text))


# url_table = url + "?db={}".format(dbs[0])
# data = "show tables;"
# print(response.text)