matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
element=3

def matrixsearch(matrix,element):

    n=len(matrix[0])
    m=len(matrix)

    l=0
    r=(n*m)-1

    while l<=r:

        m=(l+r)//2

        mid=matrix[m//n][m%n]

        if mid==element:

            return True

        elif mid>element:

            r=m-1

        else:

            l=m+1

    return False

if matrixsearch(matrix,element):

    print("yes")

else:

    print("no")
