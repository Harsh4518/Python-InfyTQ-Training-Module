def maxzigzag(arr):

    n=len(arr)
    length=0
    lastsign=0

    def sinfun(n):

        if n!=0:

            if n>0:

                return 1

            else:

                return -1
        else:

            return 0
        
    for i in range(1,n):

        sign=sinfun(arr[i]-arr[i-1])

        if sign!=lastsign and sign!=0:

            lastsign=sign
            length+=1

nums=[1,17,5,10,13,15,10,5,16,8]
print(maxzigzag(nums))
        
