def sort_array(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
    return arr

arr = list(map(int, input("Enter an array of 0s, 1s, and 2s (space-separated): ").split()))
sorted_arr = sort_array(arr)
print("Sorted Array:", sorted_arr)
