#String Function

s="this is python lab in this lab"

print(s.endswith("ab"))
print(s.startswith("thi"))
print(s.count("is"))
print(s.count("is",7,15))

print(s.find("is")) #first occurance
print(s.index("is")) #first occurance

print(s.rfind("is"))
print(s.rindex("is"))

st="pythonlab"

print(st.isalpha())

st1="python lab"

print(st1.isalpha())

a="23+25j"
print(a.isnumeric())
print(a.isdigit())
print(a.isdecimal())

a="23+25j"
print(a.isnumeric())
print(a.isdigit())
print(a.isdecimal())

a="abc"
print(a.isnumeric())
print(a.isdigit())
print(a.isdecimal())

a="23abc"
print(a.isnumeric())
print(a.isdigit())
print(a.isdecimal())

a="123abc"
print(a.isalnum())

a="123 abc"
print(a.isalnum())

a="abc"
print(a.isalnum())

l=" \n \t"
print(l.isspace())

l="this is string example...wow!"
print(l.isspace())

print('_for'.isidentifier())
print("".isprintable())

_=2
print(_)

st="paris"
print(st.center(10,","))
print(st.ljust(10,","))

s="hello katty"

print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.capitalize())
print(s.title())
print(s.casefold())
print(s.zfill(20))

l="this is string example...wow!"
print(l.istitle())

d="Hello there how are you?"
print(d.split("'"))
print(d.split())
print(d.split(maxsplit=3))
print(d.rsplit(maxsplit=3))


e="0000hello there how are you0000"
print(e.strip('0'))
print(e.lstrip('0'))
print(e.rstrip('0'))

e="  katty   "
print(e.strip())
print(e.lstrip())
print(e.rstrip())

w="123Katty" #left to rigth move.
res=w.strip("123Kd")
print(res)

print("a\tb\tc".expandtabs(tabsize=20))

st="Hello world welcome to earth!"
print(st.removesuffix("earth"))
print(st.removeprefix("hello"))
print(st.removeprefix("hey"))



