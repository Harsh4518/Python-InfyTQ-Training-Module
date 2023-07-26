S="3523014"
i,j=0,1
res=[]

s=int(S[0])

while i<len(S) and j<len(S):
    
    s=s+int(S[j])
    
    if s==10:

        res.append(S[i:j+1])

        if S[j+1]==0:

            res.append(S[i:j+2])

            
        i+=1
        s=int(S[i])
        j=i+1

print(res)
