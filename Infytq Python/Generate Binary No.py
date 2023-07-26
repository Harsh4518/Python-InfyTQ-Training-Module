def generate(n):

    queue.append('1')
    
    for i in range(n):

        first=queue.pop(0)
        queue.append(first+'0')
        queue.append(first+'1')

        print(first,end=' ')


queue=[]
n=16
generate(n)
