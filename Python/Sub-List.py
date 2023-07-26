a=[1,2,3,4]

list1=[[]]

for i in range(len(a)+1):

    for j in range(i):

        res=a[j:i]

        list1.append(res)

print("All Possible Sub-list:{}".format(list1))
