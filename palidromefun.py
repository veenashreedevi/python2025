def is_palindrome(s)
    cleaned_string = ''.join(e for e in s if e.isalnum()).lower()
    return cleaned_string == cleaned_string[::-1]
input_str = "A man a plan a canal Panama"
result = is_palindrome(input_str)

if result:
    print(f"'{input_str}' is a palindrome.")
else:
    print(f"'{input_str}' is not a palindrome.")
