#Lambda function.

f=lambda x,y:x if x>y else y
print(f(4,5))

a=[1,2,3,4,5]

b=lambda x:(b(x[1:])+x[:1] if x else [])
print(b(a))
