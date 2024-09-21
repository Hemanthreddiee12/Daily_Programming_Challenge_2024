def longest_palindrome(s):
    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""

    for i in range(len(s)):
        odd_palindrome = expand_around_center(s, i, i)

        even_palindrome = expand_around_center(s, i, i + 1)

        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        if len(even_palindrome) > len(longest):
            longest = even_palindrome

    return longest

user_input = input("Enter a string: ")

print("Longest Palindromic Substring:", longest_palindrome(user_input))
