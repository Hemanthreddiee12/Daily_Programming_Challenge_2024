def reverse_words(s):
    words = s.split()
    words.reverse()
    
    return ' '.join(words)

user_input = input("Enter the string: ")
result = reverse_words(user_input)

print(f"Reversed string: '{result}'")
