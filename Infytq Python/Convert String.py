s1="abb"
s2="baa"

total=0

for i in range(len(s1)):

    if s1[i]!=s2[i]:

        if i<len(s1)-1 and s1[i+1]!=s2[i+1]:

            s1=s1[:i]+s1[i+1]+s1[i]+s1[i+2:]
            total+=1

        else:

            total+=1

print(total)

        

    
