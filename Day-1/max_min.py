def min_max(a):
    min=a[0][0]
    max=a[0][0]
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j]<min:
                min=a[i][j]
            if a[i][j]>max:
                max=a[i][j]
    return min,max
a=[[1,2,3],[4,5,6],[7,8,9]]
print(min_max(a))