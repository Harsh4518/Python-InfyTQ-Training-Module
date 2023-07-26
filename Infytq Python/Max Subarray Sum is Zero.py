def maxlen(arr):

    h={}
    max_len=0
    curr_sum=0

    for i in range(len(arr)):

        curr_sum+=arr[i]

        if curr_sum==0:

            max_len+=1

        if curr_sum in h:

            max_len=max(max_len,i-h[curr_sum])

        else:

            h[curr_sum]=i

    return curr_sum

arr=[15,-2,2,-8,1,7,10,13]
print(maxlen(arr))
