from multiprocessing import Process
import random
from multiprocessing import Pool, cpu_count

def pi_approx(n: int):
    in_circle = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if pow(x,2) + pow(y,2) <= 1:
            in_circle += 1

    pi = 4 * in_circle / n
    print(f'PI: {pi}')

def main():

    print(f'starting computations on {cpu_count()} cores')

    number_of_runs = 100000

    with Pool() as p:
        pi_approx(number_of_runs)

if __name__ == '__main__':
    main()