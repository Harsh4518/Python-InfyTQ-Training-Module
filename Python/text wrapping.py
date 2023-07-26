import textwrap

string = input("Enter a string:")

width = int(input("Enter the Width:"))

str2 = textwrap.fill(string, width)

print(str2)
