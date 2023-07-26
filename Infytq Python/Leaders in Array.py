arr=[16,17,4,3,5,2]

ans=[]*len(arr)
stack=[]

for i in range(len(arr)-1,-1,-1):

    if stack==[]:

        ans.append(-1)

    elif stack!=[] and arr[i]<stack[-1]:

        ans.append(stack[-1])

    elif stack!=[] and arr[i]>=stack[-1]:

        while stack!=[] and arr[i]>=stack[-1]:

            stack.pop()

        if stack==[]:

            ans.append(-1)

        else:

            ans.append(stack[-1])

    stack.append(arr[i])

output=[]
ans=ans[::-1]
for i in range(len(ans)):

    if ans[i]==-1:

        output.append(arr[i])

print(output)
