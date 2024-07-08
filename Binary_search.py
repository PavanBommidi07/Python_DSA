def binary_search(arr,target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]< target:
            left = mid+1
        else:
            right = mid-1

array = [2,3,4,5,6]
target = 4 
val = binary_search(array,target)
print(val)