from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, long(pow(n, 0.5) + 1)) if n % i == 0)))