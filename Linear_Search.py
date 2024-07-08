def l_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            print("found element ", value,i)
            break
array = [1,2,3,4,5]
t = 3
l_search(array,t)
