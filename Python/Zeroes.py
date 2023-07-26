a=[1,9,8,4,0,0,2,7,0,6,9,0]
l=[0]*(a.count(0))

arr=list(filter(lambda x:x!=0,a))

print(arr+l)



