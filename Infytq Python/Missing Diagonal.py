matrix=[[0,7,6],[9,0,1],[4,3,0]]

prev_sum=0

for i in matrix:

    prev_sum+=sum(i)

new_sum=prev_sum//2

for i in matrix:

    element=new_sum-sum(i)

    t=i.index(0)

    i[t]=element

print(matrix)
