import numpy as np

my_matrix = np.array([[1,4,9],[2,7,5],[3,8,10]])

print(my_matrix)

print(my_matrix[0][2])

def rotateMatrix(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n-layer-1
        for i in range(first, last):
            top = matrix[layer][i]            #save top element
            matrix[layer][i] = matrix[-i-1][layer]  #left element to top
            matrix[-i-1][layer] = matrix[-layer-1][-i-1] #bottom element to left
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]  #right to bottom
            matrix[i][-layer-1] = top # top to right
    return matrix

print(rotateMatrix(my_matrix))

def rotateMatrix2(matrix):  #minor change from my side
    n = len(matrix)
    first = layer = 1
    last = n-layer-1
    for i in range(first, last):
        top = matrix[layer][i]            #save top element
        matrix[layer][i] = matrix[-i-1][layer]  #left element to top
        matrix[-i-1][layer] = matrix[-layer-1][-i-1] #bottom element to left
        matrix[-layer-1][-i-1] = matrix[i][-layer-1]  #right to bottom
        matrix[i][-layer-1] = top # top to right
    return matrix

print(rotateMatrix2(my_matrix))


N = int(input('N : '))

for i in range(N):
  for j in range(2*N+1):
    if j == i:
      print(j)
    else:
      print('0')
  print()

  for n in range(100, 10, -10):
      print(n)