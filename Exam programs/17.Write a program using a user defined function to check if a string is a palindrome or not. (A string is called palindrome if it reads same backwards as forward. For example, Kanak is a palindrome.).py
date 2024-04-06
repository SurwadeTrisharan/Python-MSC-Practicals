'''def is_palindrome(s):
    s = s.lower()
    s = s.replace(" ", "")
    return s == s[::-1]
# Get user input
user_input = input("Enter a string: ")
# Check if the input string is a palindrome
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome string.")
else:
    print(f"{user_input} is not a palindrome string.")
'''
def is_palindrome(s):
    s = s.lower().replace(' ', '')
    first, last = 0, len(s) - 1
    while first < last:
        if s[first] != s[last]:
            return False
        first += 1
        last -= 1
    return True

user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome!")
else:
    print(f"{user_input} is not a palindrome.")

