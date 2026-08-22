c = input("Enter a character: ")
if c.isupper():
    print(f"{c} is an uppercase letter.")

if c.islower():
    print(f"{c} is a lowercase letter.")

if c.isdigit():
    print(f"{c} is a digit.")
    
if not c.isalnum():
    print(f"{c} is a special character.")
    