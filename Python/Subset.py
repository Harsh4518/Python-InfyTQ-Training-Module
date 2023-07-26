from collections import Counter
arr1={5,4,3,2,1}
arr2={9,8,7,6}

A=Counter(arr1)
B=Counter(arr2)

res=A&B

if res==A or res==B:

    print("True")

else:

    print("False")


