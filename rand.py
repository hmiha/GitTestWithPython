from random import Random

def randlist(n, nmax):
    items = range(n)
    r = Random()

    r.shuffle(items)
    return items

items = randlist(5,1)
print items
