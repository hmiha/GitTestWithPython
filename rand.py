import random
import time

def randlist(n, nmax):
    list = n*[0]
    for i in range(n):
        list[i] = random.uniform(0,nmax)
    return list

def quick_sort(list, left, right):
    if left >= right:
        return
    pivot = list[(left + right) // 2]

    i, j = left, right

    while True:
        while pivot > list[i]:
            i += 1
        while pivot < list[j]:
            j -= 1
        if i >= j:
            break
        else:
            list[i], list[j] = list[j], list[i]
            i, j = i + 1, j - 1
    quick_sort(list, left, i - 1)
    quick_sort(list, j + 1, right)


t = time.clock()

list = randlist(100, 1)
quick_sort(list, 0, len(list) - 1 )

print time.clock() - t
