matrix=[[3,7,0,9,8],[5,3,7,0,9],[4,6,5,3,7]]

for i in range(len(matrix)-1):

    for j in range(len(matrix[0])-1):

        if matrix[i][j]!=matrix[i+1][j+1]:

            flag=0

        else:

            flag=1

if flag==1:

    print("Not A Toeplitz matrix")

else:

    print("Toeplitz Matrix")
