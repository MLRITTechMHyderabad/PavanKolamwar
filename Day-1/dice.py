import random
R=int(input("enter no of rounds:"))
rows, cols = 3, 4
matrix = [[0] * cols for _ in range(rows)]
for i in range(len(matrix)):
    for j in range(i,len(matrix[i])):
        x=random.randint(1, 7)
        matrix[i][j]=x
        
#=random.randomint(1,7)
print(matrix)

for i in range(1,7):
    count=0
    for j in range(1,7):
        if i+j==8:
            count=count+1
            
print(count)
