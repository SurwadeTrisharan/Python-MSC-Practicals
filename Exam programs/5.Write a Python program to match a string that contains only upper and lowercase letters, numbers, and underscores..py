import re

def is_valid_string(string):
    # Define a regular expression pattern to match the string
    pattern = r'^[a-z,A-Z,0-9_]+$'
    
    # Use re.match() to check if the string matches the pattern
    if re.match(pattern, string):
        return True
    else:
        return False

# Get input string from the user
string = input("Enter a string: ")

# Check if the input string is valid
if is_valid_string(string):
    print("The string contains only upper and lowercase letters, numbers, and underscores.")
else:
    print("The string contains characters other than upper and lowercase letters, numbers, and underscores.")
