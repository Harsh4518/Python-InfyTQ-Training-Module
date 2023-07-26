arr=[2,5,3,7,8,1,9]
ans=[]
stack=[]

for i in range(len(arr)):

    if stack==[]:

        ans.append(-1)

    elif stack!=[] and stack[-1]<arr[i]:

        ans.append(stack[-1])

    elif stack!=[] and stack[-1]>=arr[i]:

        while stack!=[] and stack[-1]>=arr[i]:

            stack.pop()

        if stack==[]:

            ans.append(-1)

        else:

            ans.append(stack[-1])

    stack.append(arr[i])

print(ans)
    
