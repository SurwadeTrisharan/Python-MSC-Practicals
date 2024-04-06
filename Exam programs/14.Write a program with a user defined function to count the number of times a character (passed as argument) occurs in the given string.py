def count_char(string, char):
    count = 0
    for character in string:
        if character == char:
            count += 1
    return count

string = input("Enter a string: ")
char = input("Enter a character: ")

count = count_char(string, char)

print(f"The character '{char}' occurs {count} time(s) in the string.")
