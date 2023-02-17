fib1 = fib2 = 1
n = 10
# n = int(input())

print(fib1, end=' ')
print(fib2, end=' ')

for i in range(1, n):
    fib1, fib2 = fib2, fib1+fib2
    print(fib2, end=' ')
