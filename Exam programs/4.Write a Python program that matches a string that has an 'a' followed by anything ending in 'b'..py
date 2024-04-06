import re

def match_pattern(string):
    # Define a regular expression pattern to match the string
    pattern = r'a.*b$'
    
    # Use re.match() to check if the string matches the pattern
    if re.match(pattern, string):
        return True
    else:
        return False

# Get input string from the user
string = input("Enter a string: ")

# Check if the input string matches the pattern
if match_pattern(string):
    print(f"The string '{string}' matches the pattern: 'a' followed by anything ending in 'b'.")
else:
    print(f"The string '{string}' does not match the pattern.")
