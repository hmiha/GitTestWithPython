def binary_search(list,key):
    low = 0
    hi = len(list) - 1

    
    while low <= hi:
        #割り算で小数点以下切り捨ては//
        mid = (hi + low) // 2
        if list[mid] == key: 
            return("found")
        elif key < list[mid]:
            hi = mid - 1
        elif key > list[mid]:
            low = mid + 1
    
    if low > hi:
        return ("Not found")
            

list = [1, 3, 5, 7, 9]
key = input("key = ")
print binary_search(list,key)
