import multiprocessing
import os 
import time
def print_numbers():
    pid = os.getpid()
    for i in range(5):
        print(f'{i}@{pid}')
        time.sleep(0.025)

if __name__ == '__main__':
    processes=[]
    for i in range(5):
        process = multiprocessing.Process(target=print_numbers)
        processes.append(process)
        process.start()

        # processes[i].join()
    print_numbers()
