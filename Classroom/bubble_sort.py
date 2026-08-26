def bubble_sort(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(0,n-1):
            if (arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr=[bubblesor9,5,1,10,18,33,77,45]
bubble_sort(arr)
print(arr)
