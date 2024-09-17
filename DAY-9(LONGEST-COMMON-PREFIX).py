def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for string in strs[1:]:
        while string[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix

def get_user_input():
    n = int(input("Enter the number of strings: "))
    strs = []
    for i in range(n):
        strs.append(input(f"Enter string {i + 1}: "))
    return strs

def main():
    strs = get_user_input()
    result = longest_common_prefix(strs)
    print(f"Longest Common Prefix: '{result}'")

if __name__ == "__main__":
    main()
