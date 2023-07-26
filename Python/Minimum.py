n=int(input("Enter the Number of Elements:\n"))

list1=[]

for i in range(n):

    element=int(input())

    list1.append(element)

print("Elements:",list1)

print("Minimum Element",min(list1))
