#linear Search

l=[12,34,56,23,14,16,38,79,2]

def linear(l,n):

    for i in range(len(l)):

        if l[i]==n:

            return i

k=56
res=linear(l,k)

print("Element {} found at index {}.".format(k,res))
