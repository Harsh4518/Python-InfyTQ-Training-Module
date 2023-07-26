n=int(input("Enter the Number of Elements:\n"))

list1=[]

for i in range(n):
    element=int(input())

    list1.append(element)


print("Elements:",list1)

product=1

for i in range(n):
    product=product*list1[i]


print("Product of elements:",product)
