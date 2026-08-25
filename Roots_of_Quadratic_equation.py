a=int(input("Enter coefficient a: "))
b=int(input("Enter coefficient b: "))
c=int(input("Enter coefficient c: "))
discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    print("Roots are real and different.")
    print(f"Root 1 = {root1:.2f}")
    print(f"Root 2 = {root2:.2f}")
elif discriminant == 0:
    root1 = -b / (2*a)
    print("Roots are real and the same.")
    print(f"Root 1 = Root 2 = {root1:.2f}")
else:
    realPart = -b / (2*a)
    imaginaryPart = (-discriminant)**0.5 / (2*a)
    print("Roots are complex and different.")
    print(f"Root 1 = {realPart:.2f} + {imaginaryPart:.2f}i")
    print(f"Root 2 = {realPart:.2f} - {imaginaryPart:.2f}i")