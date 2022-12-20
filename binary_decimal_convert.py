def add_binary(a,b):
    n = a+b
    binary_num = format(n, 'b')
    decimal_num = int(binary_num, 2)
    print(decimal_num)
    print(binary_num)

add_binary(10, 5)
