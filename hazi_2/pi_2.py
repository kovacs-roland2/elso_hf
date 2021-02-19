
from multiprocessing import Process, Queue
import random
from multiprocessing import Pool, cpu_count

def rand_val(queue):
    in_circle = 0
    num = [random.random(), random.random()]
    if pow(num[0],2) + pow(num[1],2) <= 1:
            in_circle += 1
    queue.put(in_circle)   

def main():

    queue = Queue()

    number_of_run = 10

    processes = [Process(target=rand_val, args=(queue,)) for _ in range(number_of_run)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    results = [queue.get() for _ in processes]
    in_circle = sum(results)
    
    pi = 4 * in_circle / number_of_run
    print(f'PI: {pi}')

if __name__ == '__main__':
    main()    