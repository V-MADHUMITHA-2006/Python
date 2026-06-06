# Function to find ASCII value

def find_ascii(character):
    ascii_value = ord(character)
    return ascii_value

ch = input("Enter a character: ")

if len(ch) == 1:
    result = find_ascii(ch)
    print("Character entered :", ch)
    print("ASCII value       :", result)
else:
    print("Please enter only one character.")
