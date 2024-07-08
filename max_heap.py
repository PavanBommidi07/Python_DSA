def left(k):
    return 2*k+1
def right(k):
    return 2*k+1

def max_heap(A,k):
    l = left(k)
    r = right(k)

    if l < len(A) and A[l] > A[k]:
        largest = l
    else:
        largest = k
    if r < len(A) and A[r] > A[largest]:
       largest = r
    
    if largest != k:
        A[k], A[largest] = A[largest], A[k]

def build_max_heap(A):
    n = len(A)//2
    for i in range(n-1,-1,-1):
        max_heap(A, i)

A = [3,9,2,1,4,5]
build_max_heap(A)
print("max_heap ",A)