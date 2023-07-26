#declaration: d={} and d=dict()
#key are unique and values are non unique.
#keys can be any non-iterable.

#declaration
d1={'Name':"sara",'age':7,'class':"first"}
print(d1)

#*************************************************************************

#empty dictionary

d={}
print(d,type(d))

D=dict()
print(d,type(d))

#*************************************************************************

#adding elements

d={'A':1,'B':2}
print(d)
d['C']=3 #adds a new key value pair in the dictionary.
print(d)

d={'A':1,'B':2}
print(d)
d.update({'D':4}) #update function
print(d)

d={'A':1,'B':2}
print(d)
#d[input("Enter the Key:")]=int(input("Enter value:")) #through input
print(d)

#*************************************************************************

#accesing elements

d1={'Name':"sara",'age':7,'class':"first"}

print(d1["Name"]) #if wrong key given error is given.

print(d1.get('age')) #if wrong key is given get function returns the none instead of error.

print(d1.get('Section'))

print(d1.get('Section',"Wrong name"))

d={'A':1,'B':2,'C':3,'D':4,'E':5}

l=d.keys() #gives dict_keys object. #all keys are given.

print(l,type(l))

l1=d.values() ##gives dict_values object. #all values are given.

print(l1,type(l1))

l3=d.items() ##gives dict_items object. #all (key,value) pairs are given.
print(l3,type(l3))

#*************************************************************************

#nested dictionary

d={1:['a','b','c'],2:['d','e','f']}
print(d[1])
print(d[1][1])
d[1][2]='m'
print(d)

d={1:{3:'a',4:'b',5:'c'},6:{7:'d',8:'e'}}
print(d[1])
print(d[1][3])
d[1][3]='z'
print(d)

#*************************************************************************

#dict function to create dictionary.

pairs=[('k1','v1'),('k2','v2'),('k3','v3')]
d=dict(pairs)
print(d)

seq={'name','age','mobile'}
d1=dict.fromkeys(seq)
print(d1)

d2={}
d2=d2.fromkeys(seq,10)
print(d2)

d1=dict.fromkeys("abcd")
print(d1)

#enumerate function

l1=[1,2,3,4]
for i in enumerate(l1): #generates (index,value) pair.
    print(i)

l=['a','b','c','d']
d={i:j for i,j in enumerate(l)} # creating dict of index value pair.
print(d)


l={'a':1,'b':2,'c':3,'d':4}
d={j:i for i,j in l.items()} #reversing a dict.
print(d)


#if we are iterating over dict witour keys,values,items than we are iterating over the keys.

l={'a':1,'b':2,'c':3,'d':4,'e':5}

print(sorted(l))
print(sorted(l.items()))
print(sorted(l.values()))

#sorting through lambda function.

l={'a':1,'b':2,'c':3,'d':4,'e':5}

#print(sorted(d.items()"""Returns a tuple.""",key=lambda x:x[1])) #sorting through values.
#print(sorted(d.items()"""Returns a tuple.""",key=lambda x:x[0])) #sorting through keys.

      
#removing elements in dict.

l={'a':1,'b':2,'c':3,'d':4,'e':5}

del l['a'] #delete the specified key.
print(l)

l.pop('c') #deletes the given key,key is must.
print(l)

l.pop('f','e') #returns e since f is not present.
print(l)

l.popitem() #returns key value pair.
print(l)

l.clear() #clears all entries of a dict.
print(l)


#l.pop()
#print(l)

#del l
#print(l)












