n=int(input("Enter the no of elements:"))

list1=[]

print("Enter the elements in the list:")

for i in range(n):
    element=int(input())

    list1.append(element)

print("Element in the list:",list1)

for i in list1:

    if(i%2==0):

        list1.remove(i)

print("\nlist after removal of even elements:",list1)
        
