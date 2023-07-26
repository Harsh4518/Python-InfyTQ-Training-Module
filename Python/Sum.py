n=int(input("Enter the Number of elements:\n"))

list1=[]

for i in range(n):
    
    element=int(input())
    
    list1.append(element)

print("Elements:",list1)
 
s=sum(list1)

print("Total Sum=",s)    
