def quick_sort(array):
    if len(array)<=1:
        return array
    else:
        pivot = array[0]
        less_than_pivot = [x for x in array[1:] if x<= pivot]
        more_than_pivot = [x for x in array[1:] if x>= pivot]
        return quick_sort(less_than_pivot)+[pivot]+quick_sort(more_than_pivot)

arr = [9,4,2,5,1]
res = quick_sort(arr)
print(res)