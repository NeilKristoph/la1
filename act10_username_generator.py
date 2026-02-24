print("===== Username Generator =====")
f_name = input("Enter your full name: ")
birth_year = input("Enter your birth year: ")
parts = f_name.strip().split()

if len(parts) >= 2:
    first_name = parts[0]
    last_name = parts[-1]
    print(f"\nYour username is: {first_name[:3]}{last_name[-3:]}{birth_year[-2:]}")
else:
    print("\nPlease enter at least a first name and a last name.")
