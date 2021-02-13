def fibonacci(n: int, cache: list= [1, 1]): 
    #print(cache)
    current_len = len(cache)
    if current_len < n:
        for i in range(n - current_len):
            cache.append(cache[-2] + cache[-1])
        to_print = cache[-1]
    else:
        to_print = cache[n]
      
    #print(cache)
    print(f'The {n}th number in the Fibonacci series is {to_print}.') 
    
fibonacci(4)