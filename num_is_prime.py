def is_prime(num):
    for n in range(2, int(num * 0.5) + 1):
        if num % n == 0:
            return False
    return True


## checking numbers
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
