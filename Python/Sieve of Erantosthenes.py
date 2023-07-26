"""In Mathematics,the seive of eratosthenes is an ancient algo  
   for finding prime number upto any predefines integer n
   works under seive approach
   Works Through Elimination method.
   Complexity:(nlog(logn)).
"""

def SieveofErantosthenes(n):

    prime=[True for i in range(n+1)]
    p=2

    while(p*p<=n):

        if prime[p]==True:

            for i in range(p*2,n+1,p):

                prime[i]=False

        p+=1

    for p in range(2,n+1):

        if prime[p]:

            print(p)

n=int(input("Enter the Number:"))
SieveofErantosthenes(n)
