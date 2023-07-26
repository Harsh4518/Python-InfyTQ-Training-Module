n=int(input("Enter the decimal Number:"))
l=[]

while n!=0:

    l.append(str(n%2))
    n=n//2

l="".join(l)
l=l[::-1]

print(l)


    
