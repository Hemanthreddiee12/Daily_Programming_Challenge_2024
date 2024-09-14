def find_subarrays_with_zero_sum(arr):
    result = []
    sum_index_map = {}
    current_sum = 0

    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum == 0:
            result.append((0, i))

        if current_sum in sum_index_map:
            indices = sum_index_map[current_sum]
            for index in indices:
                result.append((index + 1, i))
            sum_index_map[current_sum].append(i)
        else:
            sum_index_map[current_sum] = [i]

    return result

def get_user_input():
    try:
        arr = list(map(int, input("Enter the array elements (space-separated): ").split()))
        return arr
    except ValueError:
        print("Invalid input.")
        return get_user_input()

def main():
    arr = get_user_input()
    subarrays = find_subarrays_with_zero_sum(arr)
    
    if subarrays:
        print("Subarrays with zero sum:", subarrays)
    else:
        print("No subarray with zero sum found.")

if __name__ == "__main__":
    main()
