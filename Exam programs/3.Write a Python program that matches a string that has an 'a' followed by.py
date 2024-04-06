import re
def match_pattern(string, pattern):
    if re.match(pattern, string):
        return True
    else:
        return False

string = input("Enter a string: ")
A = r'ab*'
B = r'ab+'
C = r'ab?'
D = r'ab{3}'
E = r'ab{2,3}'

patterns = [
            (A, "A) Zero or more 'b's"),
            (B, "B) One or more 'b's"),
            (C, "C) Zero or one 'b's"),
            (D, "D) Three 'b's"),
            (E, "E) Two to three 'b's")
           ]

for pattern, description in patterns:
    if match_pattern(string, pattern):
        print(f"The string matches pattern {description}.")
    else:
        print(f"The string does not match pattern {description}.")
