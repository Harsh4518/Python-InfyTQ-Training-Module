n=int(input("Enter the Number:"))

while True:

    if str(n)==str(n)[::-1]:

        print(n)
        break

    else:

        t=str(n)[::-1]
        n=n+int(t)
        
