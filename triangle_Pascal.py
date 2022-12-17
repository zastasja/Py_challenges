# треугольник Паскаля, матрица
layer = 4
triangle = []
for i in range(layer+1):
    triangle.append([1]+[0]*layer)
for i in range(1, layer+1):
    for j in range(1, layer+1):
        triangle[i][j] = triangle[i-1][j]+triangle[i-1][j-1]
for i in range(0, layer+1):
    for j in range(0, layer+1):
        print(triangle[i][j], end=" ")
    print()
