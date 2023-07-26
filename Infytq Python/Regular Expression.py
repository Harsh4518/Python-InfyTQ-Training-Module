import re

#1.Match (Only starting First Occurances from starting)

string="harsh works in infosys"
pattern='\w{5}' #from starting 8 characters (alnum+"_")

result=re.match(pattern,string) #match object
print(result.group(),result.span())

string="harshworks in infosys"
pattern='harsh'

result=re.match(pattern,string) #match object
print(result.group(),result.span())


#2.Search (Find First occurance of pattern can be in middle)

string="works in harsh infosys harsh"
pattern='harsh'

result=re.search(pattern,string) #match object
print(result.group(),result.span())

#3.Findall (Returns list and find all occurances,No Need of Span and group)

string="harsh works in harsh infosys harsh"
pattern='harsh'

result=re.findall(pattern,string) #match object
print(result)

#4.replace (Replaces the pattern with given substitute)

string="harsh works in infosys"
pattern="infosys"
rep="amazon"

result=re.sub(pattern,rep,string)
print(result)

#5.subn (Manpiluted string,no of substitutions)

string="harsh works in infosys and in infosys and in infosys"
pattern="infosys"
rep="amazon"

result=re.subn(pattern,rep,string)
print(result)

#6.split(split the string based on the given pattern)

string="harsh works in infosys"
pattern="n"

result=re.split(pattern,string)
print(result)

#7.fullmatch (Entirely matching pattern find)

string="harsh works in infosys"
pattern="harsh works in infosys"

result=re.fullmatch(pattern,string)
print(result.group(),result.span())

#8.compile ()

string="works in harsh infosys harsh"
pattern=re.compile('harsh')

print(pattern)
print(pattern.findall(string))
