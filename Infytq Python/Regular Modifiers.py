import re

#1. | (either this pattern or that pattern)

string='aman work in a infyxyz infy'
pattern="x|y"

print(re.findall(pattern,string))

#2. * (0 or more occurances of pattern before *)

string="aman work in a sss infyxyz sss infy"
pattern="ss*" 

print(re.findall(pattern,string))

#3. + (1 or more occurances of pattern before +)

string="aman work in a sss infyxyz sss infy"
pattern="ss*" 

print(re.findall(pattern,string))

#4. ? (0 or 1 occurances of pattern)

string="aman work in a sss infyxyz sss infy"
pattern="s?"

print(re.findall(pattern,string))

#5. ^ (check string start with pattern)

string="ss aman work in a sss infyxyz sss infy"
pattern="^ss"

print(re.findall(pattern,string))

#6. $ (check string end with pattern)

string="aman work in a sss infyxyz sss infy"
pattern="infy$"

print(re.findall(pattern,string))

#7. {} (pattern n times)

string="sssssaman work in a sss infyxyz sss infy"
pattern="s{4}"

print(re.findall(pattern,string))

#8. [] (provides range of values)

string="aman work in a sss infyxyz sss infy"
pattern="[a-z]"

print(re.findall(pattern,string))

#9. . (matches all character except newline)

string="aman work in a sss infyxyz sss infy"
pattern="."

print(re.findall(pattern,string))

#10. (pat1)(pat2) (pattern 1 followed by pattern 2 search)

string="ssamanss work in a sss infyxyz sss infy"
pattern="(ss)(aa)"

print(re.findall(pattern,string))








