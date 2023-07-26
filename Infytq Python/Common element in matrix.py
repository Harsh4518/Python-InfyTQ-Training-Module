matrix=[[2,4,3,8,7],[4,2,1,3,6],[3,5,2,1,3],[4,5,0,2,3]]

s=set(matrix[0])

for i in range(1,len(matrix)):

    s=s.intersection(set(matrix[i]))

print(list(s))
