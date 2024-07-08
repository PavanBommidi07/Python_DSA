def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1,len(array)):
            if array[j]<array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

arr = [10,40,20,15,30]
selection_sort(arr)
print(arr)