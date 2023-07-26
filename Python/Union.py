n=int(input("Enter the Number of elements in Set A:"))

print("Enter elements in set A:")

set1=map(int,input().split(' '))

m=int(input("Enter the Number of elements in Set B:"))

print("Enter elements in set B:")

set2=map(int,input().split(' '))

l1=set(set1)
l2=set(set2)

c3=l1.union(l2)

print("Union of the sets:",c3)

s=len(c3)

print("No of element in the set:",s)
