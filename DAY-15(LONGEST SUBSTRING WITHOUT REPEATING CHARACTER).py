def longest_unique_substring(s):
    char_index = {}
    
    start = 0
    max_len = 0

    for end in range(len(s)):
        char = s[end]
        
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        
        char_index[char] = end
        max_len = max(max_len, end - start + 1)
    
    return max_len

# Example usage
s = input("Enter the string: ")
print("Length of the longest substring without repeating characters:", longest_unique_substring(s))
