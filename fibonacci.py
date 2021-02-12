def fibonacci(n: int, cache: list= [1, 1]): 
    cache = [1,1]
    for i in range(n - 2):
        cache.append(cache[i] + cache[i+1])
    print(f'The {n}th number in the Fibonacci series is {cache[-1]}.')    
    
fibonacci(4)