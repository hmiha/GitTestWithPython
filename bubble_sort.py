def bubble_sort(list):
    n = len(list)

    for i in xrange(0, n): 
        for j in xrange(0, n - i - 1):

            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    print list            

list = [4, 5, 1, 9, 2, 3, 54, 312, 543, 645, 12, 654, 75]
bubble_sort(list)
