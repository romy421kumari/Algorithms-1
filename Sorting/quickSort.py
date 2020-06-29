def partition(arr,low,high):
    i = low - 1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quick(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quick(arr,low,pi-1)
        quick(arr,pi+1,high)

print('Enter the numbers seperated by space: ',end = '')
arr = [int(x) for x in input().split()]
quick(arr,0,len(arr)-1)
print('Sorted array:',*arr)
