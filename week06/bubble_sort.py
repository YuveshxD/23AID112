def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    
    return arr

arr=list(map(int,input("Enter the elements of the array seprated by space:").split()))
print("Sorted Array:",bubble_sort(arr))

