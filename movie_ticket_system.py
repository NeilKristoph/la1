print("=== Movie Ticket System ===")

day = input("Day (weekday/weekend): ").lower()
customer = input("Customer Type (regular/student/senior): ").lower()
time = int(input("Show time (9-22): "))
tickets = int(input("Number of tickets: "))

if time < 9 or time > 22:
    print("Invalid movie time! Movies run from 9 to 22 only.")
elif tickets <= 0:
    print(" Number of tickets must be positive.")
elif day not in ["weekday", "weekend"]:
    print("Invalid day type.")
elif customer not in ["regular", "student", "senior"]:
    print("Invalid customer type.")
else:
    if day == "weekend":
        price = 300
    else:
        price = 200

    subtotal = price * tickets

    customer_discount = 0
    matinee_discount = 0
    group_discount = 0

    if customer == "student":
        customer_discount = subtotal * 0.20  # 20% off
    elif customer == "senior":
        customer_discount = subtotal * 0.30  # 30% off

    if time < 12:
        matinee_discount = (subtotal - customer_discount) * 0.10  # Extra 10% off

    if tickets >= 5:
        group_discount = (
            subtotal - customer_discount - matinee_discount
        ) * 0.05  # Extra 5% off

    total = subtotal - customer_discount - matinee_discount - group_discount

    print("\n--- RECEIPT ---")
    print(f"Base price: {price:.2f} x {tickets} = {subtotal:.2f}")

    if customer_discount > 0:
        if customer == "student":
            print(f"Student discount (20%): -{customer_discount:.2f}")
        else:
            print(f"Senior discount (30%): -{customer_discount:.2f}")

        if matinee_discount > 0:
            print(f"Matinee discount (10%): -{matinee_discount:.2f}")

        if group_discount > 0:
            print(f"Group discount (5%): -{group_discount:.2f}")

        print(f"\nTOTAL: {total:.2f}")
        print("Thank you for your purchase!")
