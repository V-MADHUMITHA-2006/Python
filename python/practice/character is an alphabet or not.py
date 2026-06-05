# Program to check if a character is an alphabet or not

ch = input("Enter a character: ")

if len(ch) == 1 and ch.isalpha():
    print("The character is an alphabet.")
else:
    print("The character is not an alphabet.")
