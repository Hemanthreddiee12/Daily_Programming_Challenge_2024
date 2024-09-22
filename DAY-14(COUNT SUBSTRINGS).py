def count_k_distinct_substrings(s, k):
    count = 0
    
    for start in range(len(s)):
        distinct_chars = {}
        distinct_count = 0
        
        for end in range(start, len(s)):
            char = s[end]
            
            if char not in distinct_chars:
                distinct_chars[char] = 1
                distinct_count += 1
            else:
                distinct_chars[char] += 1

            if distinct_count == k:
                count += 1

            elif distinct_count > k:
                break

    return count

s = input("Enter the string: ")
k = int(input("Enter the value of k: "))

result = count_k_distinct_substrings(s, k)
print("Number of substrings with exactly", k, "distinct characters:", result)
