def find_duplicate(arr):
    slow = arr[0]
    fast = arr[0]
    
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break

    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    
    return slow

def get_user_input():
    while True:
        try:
            arr = list(map(int, input("Enter the array elements (space-separated): ").split()))
            n = len(arr) - 1
            if all(1 <= x <= n for x in arr):
                return arr
            else:
                print(f"Elements must be between 1 and {n}")
        except ValueError:
            print("Invalid input")

def main():
    arr = get_user_input()  
    duplicate_number = find_duplicate(arr)  
    print("Duplicate number:", duplicate_number)

if __name__ == "__main__":
    main()
