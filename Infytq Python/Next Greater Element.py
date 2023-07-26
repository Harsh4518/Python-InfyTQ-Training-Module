l=[10,4,6,7,5,7]

stack=[]
ans=[]*(len(l))

for i in range(len(l)-1,-1,-1):

    if stack==[]:

        ans.append(-1)

    elif stack!=[] and stack[-1]>l[i]:

        ans.append(stack[-1])

    elif stack!=[] and stack[-1]<l[i]:

        while stack!=[] and stack[-1]<l[i]:

            stack.pop()

        if stack==[]:

            ans.append(-1)

        else:

            ans.append(stack[-1])

    stack.append(l[i])

result=[]

for i in range(len(l)):

    if ans[i]==-1:

        result.append(l[i])

print(result)
