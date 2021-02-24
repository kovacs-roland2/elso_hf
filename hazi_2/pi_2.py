from multiprocessing import Process, Queue
import random
from multiprocessing import Pool, cpu_count

def rand_val(queue, n):
    in_circle = 0
    for i in range(n):
      num = [random.random(), random.random()]
      if pow(num[0],2) + pow(num[1],2) <= 1:
            in_circle += 1
    queue.put(in_circle)   

def main(number_of_run):

    queue = Queue()

    processes = [Process(target=rand_val, args=(queue, int(number_of_run/cpu_count()))) for _ in range(cpu_count())]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    results = [queue.get() for _ in processes]
    in_circle = sum(results)
    
    pi = 4 * in_circle / number_of_run
    print(f'PI: {pi}')

if __name__ == '__main__':
    main(100000) 