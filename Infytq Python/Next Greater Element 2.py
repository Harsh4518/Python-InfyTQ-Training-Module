arr=[2,7,3,5,4,6,8]
ans=[]
stack=[]

for i in range(len(arr)-1,-1,-1):

    if stack==[]:

        ans.append(-1)

    elif stack!=[] and stack[-1]>arr[i]:

        ans.append(stack[-1])

    elif stack!=[] and stack[-1]<=arr[i]:

        while stack!=[] and stack[-1]<=arr[i]:

            stack.pop(0)

        if stack==[]:

            ans.append(-1)

        else:

            ans.append(stack[-1])

    stack.append(arr[i])

print(ans[::-1])
    
