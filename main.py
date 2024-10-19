# YOUR CODE HERE

def summation():
    for i in range(n):
        x = lst1[i]+lst2[i]
        updated_list.append(x)
    return print(updated_list)

def find_min_max():
    updated_list.sort()
    return print(f'({updated_list[0]},{updated_list[-1]})')

n=int(input())
lst1=[]
lst2=[]
updated_list=[]

for i in range(n):
    x=int(input())
    lst1.append(x)

for i in range(n):
    y=int(input())
    lst2.append(y)

summation()
find_min_max()
