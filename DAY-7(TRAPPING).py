def trap(height):
    if len(height) < 3:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    total_water = 0

    while left <= right:
        if left_max <= right_max:
            if height[left] < left_max:
                total_water += left_max - height[left]
            else:
                left_max = height[left]
            left += 1
        else:
            if height[right] < right_max:
                total_water += right_max - height[right]
            else:
                right_max = height[right]
            right -= 1

    return total_water

def get_user_input():
    try:
        height = list(map(int, input("Enter the heights of the bars (space-separated): ").split()))
        if len(height) < 1:
            raise ValueError("The array must have at least one element.")
        return height
    except ValueError as e:
        print(f"Invalid input: {e}")
        return get_user_input()

def main():
    height = get_user_input()
    result = trap(height)
    print(f"Total trapped rainwater: {result} units")

if __name__ == "__main__":
    main()
