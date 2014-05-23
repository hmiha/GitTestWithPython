def linear_search(seq, key):
    for i in range(0, len(seq)):
        if key == seq[i]:
            return True

    return False

def binary_search(seq, key):
    low = 0
    hi = len(seq) - 1

    while low <= hi:
        mid = (low + hi) // 2
        if key < seq[mid]:
            hi = mid - 1
        elif key > seq[mid]:
            low = mid + 1
        else: 
            return True
    return False


if __name__ == '__main__':
    seq = [1,3,5,7,9,12,32,56,65,78]

    #print seq
    for key in [34,65,78,90]:
        print "key = ", key
        print "linear", linear_search(seq,key)
        print "binary", binary_search(seq,key)

