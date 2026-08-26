A=float(input("Enter the length of side A: "))
B=float(input("Enter the length of side B: "))
C=float(input("Enter the length of side C: "))
if A<=0 or B<=0 or C<=0:
    print("Invalid input. Lengths must be positive numbers.")
else:
    if A==B==C:
        print("The triangle is equilateral.")
    elif A==B or B==C or A==C:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
        