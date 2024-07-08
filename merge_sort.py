def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        left_half = merge_sort(arr[:mid])
        right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)
def merge(left, right):
    sorted_arr = []
    i=j=0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

array = [49, 50, 20,55,1,4]
print("given  array : ", array)
sorted_array = merge_sort(array)
print(sorted_array)