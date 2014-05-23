def selection_sort(list):
    n = len(list)
    
    for i in xrange(0, n):
        k = i

        for j in xrange(i+1, n):
            if list[j] < list[k]:
                k = j
        list[i], list[k] = list[k], list[i] 
    print list


list = [4, 5, 1, 9, 2, 3]
selection_sort(list)
