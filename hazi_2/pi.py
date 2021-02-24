from multiprocessing import Process
import random
from multiprocessing import Pool, cpu_count

def pi_approx(n):
    in_circle = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if pow(x,2) + pow(y,2) <= 1:
            in_circle += 1
        
    return in_circle

def main(number_of_runs):

    print(f'starting computations on {cpu_count()} cores')

    values = ([int(number_of_runs / cpu_count())] * cpu_count())

    with Pool() as p:
        in_circle = p.map(pi_approx, values)

    pi = 4 * sum(in_circle) / number_of_runs
    print(f'PI: {pi}')

if __name__ == '__main__':
    main(100000)