arr=[1,9,4,3]
k=3

if len(set(arr))!=1:

    print("0")

else:

    b=[0]*k
    for i in range(len(arr)):

        b[i]=arr[i]^k

    for i in range(len(arr)):

        for j in range(len(b)):

            if arr[i]==b[j] and i!=j:

                print("1")
                break

    if len(set(b))!=len(b):

        print("2")

    else:

        print("-1")

        