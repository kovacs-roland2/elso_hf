from multiprocessing import Process
import random

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
    p = Process(target=pi_approx, args=(100000,))
    p.start()

if __name__ == '__main__':
    main()