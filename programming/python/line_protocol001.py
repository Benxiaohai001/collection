#! /usr/bin/env python3
import random
import string
import sys
import threading
from tqdm import tqdm
from collections import deque
from datetime import datetime

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = deque(maxlen=capacity)
        self.lock = threading.Lock()
        self.full_condition = threading.Condition(self.lock)
        self.empty_condition = threading.Condition(self.lock)

    def put(self, item):
        with self.lock:
            while len(self.buffer) == self.capacity:
                self.full_condition.wait()
            self.buffer.append(item)
            self.empty_condition.notify()

    def get(self):
        with self.lock:
            while len(self.buffer) == 0:
                self.empty_condition.wait()
            item = self.buffer.popleft()
            self.full_condition.notify()
            return item

def lp_generator_thread(start_time, end_time, interval, ring_buffer):
    print('Starting line-protocol generator thread...')

    tb_name = 'testtb'
    tags = [f'{i:04}' for i in range(10000)]
    tag_index = 0

    buf = ''
    max_buf_size = 1024 * 1024 * 100  # 100MB
    while start_time <= end_time:
        tag = f'tag={tags[tag_index]}'
        tag_index = (tag_index + 1) % len(tags)
        random_strings = [''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(10, 40))) for _ in range(200)]
        # random_ints = [random.randint(1, 100000) for _ in range(150)]
        random_ints = [f"{random.randint(1, 100000)}i" for _ in range(150)]
        random_doubles = [round(random.uniform(1.0, 100000.0), 4) for _ in range(150)]
        combined_data = random_ints + random_doubles
        # tag = f'tag={random_strings[0]}'
        field_str_set = ",".join([f'field_str{i}="{random_strings[i]}"' for i in range(200)])
        field_set = ",".join([f"field{i}={combined_data[i]}" for i in range(300)])
        buf += f"{tb_name},{tag} {field_str_set},{field_set} {start_time}\n"
        start_time += interval
        if len(buf) > max_buf_size:
            ring_buffer.put(buf)
            buf = ''

    if len(buf) > 0:
        ring_buffer.put(buf)
    ring_buffer.put('STOP')

def lp_writer_thread(file_name, ring_buffer, total_size=100):
    print('Starting line-protocol writer thread...')

    with open(file_name, mode='w', newline='') as file:
        progress_bar = tqdm(total=total_size, unit='MB', unit_scale=True)
        while True:
            data = ring_buffer.get()
            if data == 'STOP':
                print('Finished generating line-protocol file. Exiting...')
                break
            
            first_line = data.split('\n', 1)[0]
            timestamp = int(first_line.rsplit(' ', 1)[-1])
            timestamp = datetime.fromtimestamp(timestamp / 1e9)
            print(f'Timestamp of the first line: {timestamp}')

            file.write(data)
            progress_bar.update(len(data))
        progress_bar.close()

def main():
    file_name = 'lp_20240314_1800.txt'
    start_time = 1577808000000000000
    end_time = 1577811600000000000
    interval = 60_000_000_0

    script_name = sys.argv[0]
    args = sys.argv[1:]
    args_i = 0
    while args_i < len(args):
        arg = args[args_i]
        args_i += 1
        if arg == '-h' or arg == '--help':
            print(f"Usage: python3 {script_name} -o <output_file> --start <start_timestamp> --end <end_timestamp> -i <interval_nanoseconds>")
            return
        elif arg == '-o' or arg == '--output':
            file_name = args[args_i]
            args_i += 1
        elif arg == '--start':
            start_time = int(args[args_i])
            args_i += 1
        elif arg == '--end':
            end_time = int(args[args_i])
            args_i += 1
        elif arg == '-i' or arg == '--interval':
            interval = int(args[args_i])
            args_i += 1
        else:
            print(f'Unknown argument: {arg}')
            print(f"Usage: python3 {script_name} -o <output_file> --start <start_timestamp> --end <end_timestamp> -i <interval_nanoseconds>")
            return
    print(f'file_name: {file_name}, start_time: {start_time}, end_time: {end_time}, interval: {interval}')

    ring_buffer = RingBuffer(capacity=5)
    consumer = threading.Thread(target=lp_writer_thread, args=(file_name, ring_buffer,))
    producer = threading.Thread(target=lp_generator_thread, args=(start_time, end_time, interval, ring_buffer,))

    consumer.start()
    producer.start()

    consumer.join()
    producer.join()

if __name__ == "__main__":
    main()