n=int(input("Enter the no of elements:"))

list1=[]

print("Enter the Elements:")

for i in range(n):
    element=int(input())

    list1.append(element)

print("Element:",list1)

k=int(input("Enter the target element:"))

print("Possible pairs Are:")
      
for i in range(len(list1)):
      temp=list1[i]
      for j in range(len(list1)):
       if(temp+list1[j]==k):
         print(temp,list1[j])
      

      
