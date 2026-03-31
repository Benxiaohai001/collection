import threading
import sys
import queue
import csv
import time
import datetime
import random
import string

start_time = 1577808000000000000
end_time = 1577811600000000000
interval = 6000000



def generate_data(q, start_time, end_time, interval):
    buffer = ""
    while start_time <= end_time:
        random_strings = [''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(10, 40))) for _ in range(200)]
        random_ints = [random.randint(1, 100000) for _ in range(150)]
        random_doubles = [round(random.uniform(1.0, 100000.0), 4) for _ in range(150)]
        combined_data = random_ints + random_doubles
        tag = f'tag={random_strings[0]}'
        field_str_set = ",".join([f'field_str{i}="{random_strings[i+1]}"' for i in range(199)])
        field_set = ",".join([f"field{i}={combined_data[i]}" for i in range(300)])
        line = f"testtb,{tag} {field_str_set},{field_set} {start_time}"
        buffer += line + "\n"
        if sys.getsizeof(buffer) >= 100 * 1024 * 1024:  # 100MB
            q.put(buffer)
            buffer = ""
        start_time += interval
    if buffer:
        q.put(buffer)

def write_to_disk(q, filename):
    with open(filename, 'w', newline='') as file:
        while True:
            line = q.get()
            if line is None:
                break
            file.write(line + "\n")

def line_protocol(start_time, end_time, interval, filename):
    q = queue.Queue()
    t1 = threading.Thread(target=generate_data, args=(q, start_time, end_time, interval))
    t2 = threading.Thread(target=write_to_disk, args=(q, filename))
    t1.start()
    t2.start()
    t1.join()
    q.put(None)
    t2.join()

line_protocol(start_time, end_time, interval, 'data.txt')