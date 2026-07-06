#method 1 - brute force -> TC = O((n+m)(n*m)+(n*m)) SC -> O(1)
def setinfinity(matrix, row, col):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        if matrix[i][col] != 0:
            matrix[i][col] = float('inf')
    for i in range(cols):
        if matrix[row][i] != 0:
            matrix[row][i] = float('inf')
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
rows = len(matrix)
cols = len(matrix[0])
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 0:
            setinfinity(matrix, i, j)
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == float('inf'):
            matrix[i][j] = 0
print(matrix)