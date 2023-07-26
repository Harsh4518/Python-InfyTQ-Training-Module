#exception Handling
#all errors in python belongs to class Exception.

#1.Zero Division Error.

a=10
try:

    print(a/0)

except (ZeroDivisionError,NameError): #single except multiple errors.

    print("zero division error is handle.")


except NameError as argument: #define Exception.

    print("Name Error is handle.",argument)

except: #default except used at the last

    print("Error is handle")

else: #try doesn't throw any error then else will be executed as usual (try<->else) (at last always).

    print("Hello")

finally: #always executed don't depend on try,even if except not present.
        
    print("Yes")

#2.Type Error.
when we datatype is incompatible.
eg: int + string.

#3.Value Error.
when type is correct but value passed to function is incorrect.
eg: factorial(-1)

#4.assertion
User Defined Exception

a=10
b=20

assert(a>b) ,"a is not greater than that of b"
print(a-b)

























    
