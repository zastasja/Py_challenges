#Factorial from big and small number

#Example 1

import threading
from sys import setrecursionlimit

def factorial(num, mod):
    if num == 0:
        return 1
    return (num * factorial(num - 1, mod)) % mod


def factorial_big_num():
    mod = 10 ** 9 + 7
    num = int(input())
    fac = factorial(num, mod)
    print(fac)


setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)
thread = threading.Thread(target=factorial_big_num)
thread.start()

#Example 2
import math
def factorial_small_num():
    num = int(input())
    fac = math.factorial(num)
    print(fac)
factorial_num()

#Example 3
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

for n in range(1, 6):  # testing
    print(n, factorial_function(n))

