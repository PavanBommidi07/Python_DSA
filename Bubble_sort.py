def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
array = [20,10,32,40,30]
value = bubble_sort(array)
print(value)