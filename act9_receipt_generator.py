print("===== Receipt Generator =====")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity: "))
item = input("Enter the name of the item: ")
total = price * quantity

print(f"|{'Item':<15}|{'Qty':>5}|{'Price':>12}|")
print(f"|{item:<15}|{quantity:>5}|₱{price:>12,.2f}|")
print(f"|{'Total':<15}|{'':>5}|₱{total:>12,.2f}|")
