import random

def randlist(n, nmax):
    list = n*[0]
    for i in range(n):
        list[i] = random.uniform(0,nmax)
    return list

list = randlist(5, 1)
print list
