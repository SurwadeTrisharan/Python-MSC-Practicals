def write(text):
    # Open the file in write mode
    with open("text_file.txt", "w") as file:
        # Write the text to the file
        file.write(text)

def read():
    # Open the file in read mode
    with open("text_file.txt", "r") as file:
        # Read the contents of the file
        text = file.read()
        return text

# Get input string from the user
input_text = input("Enter a string: ")

# Write the input string to the text file
write(input_text)

# Read the text from the file
file_text = read()

# Display the text on the screen
print("Text read from file:")
print(file_text)
