def subarraysum(arr,n,s):

    current=arr[0]
    start=0

    i=1

    while i<=n:

        while currentsum>s and start<i-1:

            current=current-arr[start]
            start+=1

        if currentsum==s:

            print("sum found between indexes %d and %d"

            return 1

        if i<n:

            current=current+arr[i]

        i+=1

    print("No subarray found")

    return 0

    




            

    
