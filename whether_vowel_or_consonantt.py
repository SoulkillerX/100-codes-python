c = input("Enter a character: ")

if c.upper() in 'AEIOU' or c.lower() in 'aeiou':
    print(f"{c} is a vowel.")
else:
    print(f"{c} is not a vowel.")