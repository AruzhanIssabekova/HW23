import time
from datetime import datetime
from multiprocessing import Process
import os
def create_file(filename):
    time.sleep(1)
    with open(filename, 'w') as file:
        file.write("Hello world!")

if __name__ == '__main__':
    start_time = datetime.now()
    for i in range(100):
        filename = f'file{i}.txt'
        create_file(filename)
    end_time = datetime.now()
    time = end_time - start_time
    print(time)

if __name__ == '__main__':
    start_time = datetime.now()
    processes = []
    for i in range(100):
        filename = f'file_{i}.txt'
        pr = Process(target=create_file, args=(filename,))
        processes.append(pr)
        pr.start()
    for pr in processes:
        pr.join()
    end_time = datetime.now()
    time = end_time - start_time
    print(time)


