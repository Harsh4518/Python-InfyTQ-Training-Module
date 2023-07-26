matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
element=3

def binarysearch(arr,element):

    low=0
    high=len(arr)

    while low<=high:

        mid=(low+high)//2

        if arr[mid]==element:

            return mid

        elif arr[mid]>element:

            high=mid-1

        else:

            low=mid+1

    else:

        return -1

result=-1

for i in matrix:

    result=binarysearch(i,element)

    if result!=-1:

        print(result)
        break

else:

    print("Not Found!")
