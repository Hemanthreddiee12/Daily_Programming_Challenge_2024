def find_missing_number(arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    arr_sum = sum(arr)
    return total_sum - arr_sum

def get_user_input():
    try:
        arr = list(map(int, input("Enter the array elements (space-separated): ").split()))
        if not all(1 <= x <= len(arr) + 1 for x in arr):
            raise ValueError("Array elements must be between 1 and n, inclusive.")
        return arr
    except ValueError as e:
        print(e)
        return get_user_input()  

def main():
    arr = get_user_input()  
    missing_number = find_missing_number(arr)  
    print("Missing number:", missing_number)  
    

if __name__ == "__main__":
    main()
