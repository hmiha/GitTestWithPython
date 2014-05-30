import random

def randlist(n, nmax):
    items = range(n)
    r = random.Random()

    r.shuffle(items)
    return items

items = randlist(5,1)
print items
