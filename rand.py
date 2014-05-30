import random
import time

def randlist(n, nmax):
    list = n*[0]
    for i in range(n):
        #list[i] = random.uniform(0,nmax)
        list[i] = random.random()
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


def selection_sort(list):
    n = len(list)
    for i in xrange(0,n):
        k = i
        for j in xrange(i+1, n):
            if list[j] < list[k]:
                k = j
        list[i], list[k] = list[k], list[i]

def bubble_sort(list):
    n = len(list)

    for i in xrange(0, n):
        for j in xrange(9, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]



t_q = time.clock()

list = randlist(10000, 1)
list_q = list 
list_s = list 
list_b = list 

quick_sort(list_q, 0, len(list_q) - 1 )

t_s = time.clock()
print "quick_sort"
print t_s - t_q

selection_sort(list_s)
print "selection_sort"
t_b = time.clock()
print t_b - t_s

print "bubble_sort"
bubble_sort(list_b)
print time.clock() - t_b

