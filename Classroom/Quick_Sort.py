def partition(arr,start,end):
    pindex = start
    pivot = arr[end]
    for i in range(start,end):
        if arr[i] <= pivot:
            arr[i],arr[pindex] = arr[pindex],arr[i]
            pindex += 1
    arr[pindex],arr[end] = arr[end],arr[pindex]
    return pindex

def quick_sort(arr,start,end):
    if start < end:
        pindex = partition(arr, start, end)
        quick_sort(arr, start, pindex-1)
        quick_sort(arr, pindex+1, end)


if __name__ == "__main__":
    arr = [10, 5, 8, 2, 15, 3, 7]
    quick_sort(arr, 0, len(arr)-1)
    print(arr)

