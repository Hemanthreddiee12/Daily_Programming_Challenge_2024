def merge(arr1, arr2, m, n):
    i = m - 1  
    j = n - 1  
    k = m + n - 1  

    arr1.extend([0] * n)

    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1

    while j >= 0:
        arr1[k] = arr2[j]
        j -= 1
        k -= 1

def get_user_input():
    arr1 = list(map(int, input("Enter the sorted elements of arr1: ").split()))
    arr2 = list(map(int, input("Enter the sorted elements of arr2: ").split()))
    return arr1, arr2

def main():
    arr1, arr2 = get_user_input()
    m = len(arr1)
    n = len(arr2)
    merge(arr1, arr2, m, n)
    print("After merging:")
    print("arr1:", arr1[:m])  
    print("arr2:", arr1[m:])  

if __name__ == "__main__":
    main()
