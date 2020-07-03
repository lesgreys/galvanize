#question 1 practice problems
import math
import timeit
starttime = timeit.default_timer()

def is_prime(x):
    n = int(math.sqrt(x)) 
    if x <= 3: 
        return True 
    if x % 2 == 0: 
        return False 
    else: 
        for i in range(n): 
            if n % i == 0: 
                return False 
            elif n % i != 0:
                return True 
print("The time the function took to run is :", timeit.default_timer() - starttime)