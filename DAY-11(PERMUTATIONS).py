def permute(s):
    def backtrack(start, end):
        if start == end:
            perm = ''.join(s)

            if perm not in result:
                result.append(perm)
        else:
            for i in range(start, end):
                s[start], s[i] = s[i], s[start]  # Swap characters
                backtrack(start + 1, end)  # Recursive call
                s[start], s[i] = s[i], s[start]  # Backtrack to original

    s = list(s)
    result = []
    backtrack(0, len(s))  # Start the backtracking process
    return result

user_input = input("Enter a string: ")
permutations = permute(user_input)

print("Permutations:", sorted(permutations))
print("Total permutations:", len(permutations))
