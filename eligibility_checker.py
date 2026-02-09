print("===== Eligibility Checker =====\n")
age = int(input("Enter your age: "))
if age >= 18:
    valid_id = (input("Do you have a valid ID? (yes/no): ")).strip().lower()
    v_id = valid_id == "yes"
    if age >= 18 and v_id:
        print("Eligible!")
        if age >= 60 and v_id:
            print("✅ Senior citizen discount!")
        else:
            print("")
    else:
        print("Not eligible.")
else:
    print("Not eligible.")
