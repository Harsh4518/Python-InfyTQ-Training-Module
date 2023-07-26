s="seeksforgeeks"
t="geeksforgeekg"

s1=""
s2=""

for i in range(len(s)):

    if s[i]!=t[i]:

        s1+=s[i]
        s2+=t[i]

if len(s1)==len(s2)==2 and len(set(s1))==len(set(s2))==1:

    print("YES")

else:

    print("NO")




