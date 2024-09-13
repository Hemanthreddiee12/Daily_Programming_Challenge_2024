def find_leaders(arr):
    n = len(arr)
    leaders = []  
    max_right = arr[-1] 
    leaders.append(max_right)  
    
    for i in range(n - 2, -1, -1):  
        if arr[i] > max_right:
            leaders.append(arr[i])
            max_right = arr[i]  
    
    return leaders[::-1]  

def get_user_input():
    try:
        arr = list(map(int, input("Enter the array elements (space-separated): ").split()))
        return arr
    except ValueError:
        print("Invalid input")
        return get_user_input()

def main():
    arr = get_user_input()
    leaders = find_leaders(arr)
    print("Leaders:", leaders)

if __name__ == "__main__":
    main()
