#user defined exception

class MyfirstError(Exception):

    pass

a=10
try:

    raise Myfirsterror
    #print(a/0)
    
except MyfirstError:

    print("new error handle")

except ZeroDivisionError as x:

    print("Zero Division Error Handle",x)
