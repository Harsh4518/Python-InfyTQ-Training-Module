n=int(input("Enter the Number of Elements:\n"))

list1=[]

for i in range(n):

    element=int(input())

    list1.append(element)

print("Elements:",list1)

set1=set(list1)

set1.remove(max(set1))

print("Second Maximum Element:",max(set1))
