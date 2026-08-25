Marks=int(input("Enter your marks: "))
Total_marks=100
percentage=(Marks/Total_marks)*100
if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
elif percentage >= 60:
    print("Grade: D")
else:
    print("Grade: F")