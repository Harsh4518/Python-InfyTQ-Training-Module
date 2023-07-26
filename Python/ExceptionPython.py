#Exception Handling

print("0*******************\n\n")

"""print(a) #NameError
print(int('a')) #valueError
l=[2,3,4]
print(l[5]) #indexError """

#************************************

#try-except (exception handling)

print("1*******************")
print("hello")

try:
    print(int('a'))

except:

    print("helloworld")

print("we can still continue")
print("psit")

"""if default exception is not used
   than need to specify the error name for that particular error otherwise
   code executes at that error rest of part will not be executed."""

#************************************

#try-except(individual error)

print("2*******************")

try:
    print(0/7) #here the error is encountered then correponding to that error except is execurted.
    print(int('a'))

except ValueError: #for valueError
    print("hey")

except ZeroDivisionError: #for ZeroDivisionError
    print("hey2")
print("hello")

#************************************

#printing error Message:

print("3*******************")

try:
    print(7/0)
    print(int('a'))

except ValueError as e1: #for valueError
    print("hey",e1)

except ZeroDivisionError as e: #for ZeroDivisionError
    print("hey2",e)
print("hello")

#************************************

#else clause will be included only when no exception is generated.

print("4*******************")

l=[1]
try:
    print(l[0])
    print('a')

except ValueError as e1: #for valueError
    print("hey",e1)

except ZeroDivisionError as e: #for ZeroDivisionError
    print("hey2",e)
else:  #Runs when no exception is executed no error is there.
    print("else block")
print("Bye")

#************************************

#finaly clause it is always included whether error is reached or not.
#finally independent from except and else clause.

print("5*******************")

try:
    print(7/0)
    print(int('a'))

except ValueError as e1: #for valueError
    print("hey",e1)

except ZeroDivisionError as e: #for ZeroDivisionError
    print("hey2",e)
else:
    print("hello")
finally:
    print("Bye")
print("finally block")

#************************************

#exception is superclass of all exceptions.
#exception is written always at the last.

print("6*******************")

l=[1,2,3,4]
try:
    print(l[5])
    print(int('a'))

except ValueError as e1: #for valueError
    print("hey",e1)

except ZeroDivisionError as e: #for ZeroDivisionError
    print("hey2",e)
except Exception as e:
    print("Exception",e)
else:
    print("hello")
finally:
    print("Bye")
print("finally block")

#************************************

#commom block of all errors.

print("7*******************")

try:
    print(7/2)
    print(int('a'))

except (ValueError,ZeroDivisionError) as e:
    print("common block",e)

print("END")

#************************************

#we use raise keyword to raise an exception forcefully.

print("8*******************")

print("8")
x=10
if x>5:
    raise Exception("x should not exceed 2",x)

#************************************





