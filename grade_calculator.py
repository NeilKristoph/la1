print("===== Grade Calculator =====\n")
grade = int(input("Enter your grade (0-100): "))
if grade >= 90 and grade <= 100:
    if grade >= 97 and grade <= 100:
        print(f" Score: {grade} → Grade: (A+) - Outstanding!")
    elif grade >= 93 and grade < 97:
        print(f" Score: {grade} → Grade: A - Excellent!")
    else:
        print(f" Score: {grade} → Grade: (A-) - Very Good!")

elif grade >= 80 and grade < 90:
    if grade >= 87 and grade < 90:
        print(f" Score: {grade} → Grade: (B+) - Very Good!")
    elif grade >= 83 and grade < 87:
        print(f" Score: {grade} → Grade: B - Good!")
    else:
        print(f" Score: {grade} → Grade: (B-) - Satisfactory!")

elif grade >= 70 and grade < 80:
    if grade >= 77 and grade < 80:
        print(f" Score: {grade} → Grade: (C+) - Satisfactory!")
    elif grade >= 73 and grade < 77:
        print(f" Score: {grade} → Grade: C - Average!")
    else:
        print(f" Score: {grade} → Grade: (C-) - Below Average!")

elif grade >= 60 and grade < 70:
    if grade >= 67 and grade < 70:
        print(f" Score: {grade} → Grade: (D+) - Pass!")
    elif grade >= 63 and grade < 67:
        print(f" Score: {grade} → Grade: D - Pass!")
    else:
        print(f" Score: {grade} → Grade: (D-) - Pass!")

elif grade >= 0 and grade < 60:
    print(f" Score: {grade} → Grade: F - Fail.")
else:
    print("Invalid grade entered. Please enter a number between 0 and 100.")
