ch =input("Enter the character:")
if len(ch)==1 and ch.isalpha():
    if ch.lower()in['a','e','i','o','u']:
        print(ch ,"is vowel")
    else:
        print(ch ,"is a Constant")

else:
    print("Please enter the single alphabet.")
