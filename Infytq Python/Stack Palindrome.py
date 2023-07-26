s="geeksforgeeks"

stack=[]

for i in range(len(s)):

    stack.insert(i,s[i])

index,flag=0,1

while stack!=[]:

    temp=stack.pop(0)

    if temp==s[index]:

        flag=1

    else:

        flag=0
        break

    index+=1

if flag:

    print("Palindrome")

else:

    print("No")
    
