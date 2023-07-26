def StockBuySell(A,n):

    list1=[]
    i=0

    while i<n-1:

        while i<n-1 and A[i+1]<=A[i]:

            i+=1

        if i>n-1:

            break
        buy=i
        i+=1

        while i<n and A[i]>=A[i-1]:

            i+=1

        sell=i-1
        list1.append((buy,sell))

    return list1

A=[100,180,260,310,40,335,695]
n=len(A)
print(StockBuySell(A,n))
