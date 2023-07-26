n1=int(input("Enter the no of elements in 1st list:"))

list1=[]

print("Enter the element in list 1:")

for i in range(n1):
    element=int(input())

    list1.append(element)

print("Elements in the list 1:",list1)

n2=int(input("\nEnter the no of elements in 2nd list:"))

list2=[]

print("Enter the element in list 2:")

for i in range(n2):
    element=int(input())

    list2.append(element)

print("Elements in the list 1:",list2)

list1.extend(list2)

print("\nMerged list:",list1)

list1.sort()

print("\nMerged Sorted list:",list1)
    
    
