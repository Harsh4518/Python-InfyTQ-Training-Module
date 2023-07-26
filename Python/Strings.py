#string representation
s1='Python'
s2="Python"
s3='''Python'''
s4="""Python"""

print(s1,s2,s3,s4)

#multiline string
s="""This is online
python lab for computer science students"""
print(s)

#concatenation
a="hello"
b="world"
z=a+b
print(z)

#every operator in python is associated with special symbol __
c=a.__add__(b)
print(z)
print(a+b)
print(c)

#string multiplied certain time (concatenation)
a="hello"
print(a*2)
print(3*a)

#membership operator 
print("e" in a)
print("y" in a)

print("hello \n python")
print(r"hello \n python") #raw string escape sequence is printed
print("hello\\n python") #escape characters
print("hello\python")
print("hello\"python") #escape characters '\' used to print special characters
print("hello\\\\npython")

s="pythonlaboratory"

print(s[-1::-100])

