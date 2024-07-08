def left(k):
    return 2*k+1
def right(k):
    return 2*k+2
def min_heap(arr,k):
    l = left(k)
    r = right(k)
    if l<len(arr) and arr[l]<arr[k]:
        smallest=l
    else:
        smallest=k
    if r<len(arr) and arr[r]<arr[smallest]:
        smallest=r
    if smallest != k:
        arr[k],arr[smallest] = arr[smallest], arr[k]
def build_min_heap(arr):
    n = len(arr)//2-1
    for k in range(n,-1,-1):
        min_heap(arr, k)

arr = [3,9,2,1,4,5]
build_min_heap(arr)
print('min heap :',arr)
    