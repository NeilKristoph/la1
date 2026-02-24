print("===== Student ID Generator =====")
f_name = input("Enter your full name: ").strip()
course_code = input("Enter your course code: ").strip()
y_level = (input("Enter your year level (1 - 4): ")).strip()
b_date = input("Enter your birth date (MM/DD/YYYY): ").strip()

name_parts = f_name.split()
clean_name = " ".join(name_parts).title()
last_name = name_parts[-1].upper()
course_code = course_code.upper()
birth_year = b_date[-4:]
year_text = (
    f"{y_level}st Year"
    if y_level == "1"
    else f"{y_level}nd Year"
    if y_level == "2"
    else f"{y_level}rd Year"
    if y_level == "3"
    else f"{y_level}th Year"
)
student_id = f"{course_code}-{y_level}-{last_name}-{birth_year}"


width = 70
top_border = "╔" + "═" * (width - 2) + "╗"
middle_border = "╠" + "═" * (width - 2) + "╣"
bottom_border = "╚" + "═" * (width - 2) + "╝"

print("\n" + top_border)
print(f"║{'STUDENT ID CARD':^{width - 2}}║")
print(middle_border)
print(f"║  {'Name:':<12}{clean_name:<{width - 16}}║")
print(f"║  {'Course:':<12}{course_code:<{width - 16}}║")
print(f"║  {'Year:':<12}{year_text:<{width - 16}}║")
print(f"║{'':<{width - 2}}║")
print(f"║  {'Student ID:':<12}{student_id:<{width - 16}}║")
print(bottom_border)

print("\nID Generated Successfully!")
