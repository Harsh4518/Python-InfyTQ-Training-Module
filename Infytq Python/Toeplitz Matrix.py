matrix=[['a','b','c','d','e'],['f','a','b','c','d'],['g','f','a','b','c'],['h','g','f','a','b'],['i','h','g','f','a']]

#check matrix[i][j] is same with matrix[i+1][j+1] or not.

for i in range(len(matrix)-1):

    for j in range(len(matrix[0])-1):

        if matrix[i][j]!=matrix[i+1][j+1]:

            print("False")
            break

else:

    print("True")
