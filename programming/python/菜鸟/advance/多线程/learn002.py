import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print(f"start {self.name}")
        print_time(self.name, self.delay, 5)
        print(f"end {self.name}")

test_num = 1

def print_time(threadName, delay, counter):
    while counter:
        test_num += 1
        print(f"test_num: {test_num}")
        print(f"exitFlag: {exitFlag}")
        if exitFlag:
            return
        time.sleep(delay)
        print(f"{threadName}: {time.ctime(time.time())}")
        counter -= 1


thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(f"End main thread")