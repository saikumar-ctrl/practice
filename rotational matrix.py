rows=int(input())
cols=int(input())
matrix=[]
for i in range(rows):
    matrix.append(list(map(int,input().split())))
#transpose the matrix
for i in range(rows):
    for j in range(i,cols):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
#reverse the matrix to get rotational matrix
for i in range(cols//2):
    for j in range(rows):
        matrix[j][i],matrix[j][cols-1-i]=matrix[j][cols-1-i],matrix[j][i]
print(matrix)