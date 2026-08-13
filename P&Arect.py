# Program to calculate area and perimeter of a rectangle

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print(f"Area of the rectangle: {area}")
print(f"Perimeter of the rectangle: {perimeter}")