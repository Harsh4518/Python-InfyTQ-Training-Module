n=int(input("Enter the Number of elements:\n"))

list1=[]

print("Enter the Elements:")

for i in range(n):
    element=int(input())

    list1.append(element)

print("Elements:",list1)    

s1=set(list1)

s1.remove(min(s1))

print("Second Minimum element Present:",min(s1))
          
