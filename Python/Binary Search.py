#Binary Search

def Binary_Search(a,beg,end,k):

    if end>=beg:

        mid=(beg+end)//2

        if a[mid]==k:

            return mid

        elif a[mid]>k:

            return Binary_Search(a,beg,mid-1,k)

        else:

            return Binary_Search(a,mid+1,end,k)

    else:

        return -1

l=[12,34,56,23,14,16,38,79,2]
low=0
high=len(l)-1
k=16

res=Binary_Search(l,low,high,k)

print("Element {} found at index {}.".format(k,res))
