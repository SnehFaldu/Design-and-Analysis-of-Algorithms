#selection sort in python
def selection_sort(arr):
    n=len(arr)
    for i in range(0,n):
        min_index=i
        for j in range(i,n):
            if (arr[j]<arr[min_index]):
                min_index=j
        arr[i], arr[min_index] = arr[min_index], arr[i]
arr=[9,5,1,10,18,33,77,45]
selection_sort(arr)
print(arr)

