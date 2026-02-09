print("===== Login System =====\n")
username = "tagavilla"
password = "12345"
input_username = input("Enter your username: ")
input_password = input("Enter your password: ")
if input_username == username:
    if input_password == password:
        print("Welcome! Login successful.")
    else:
        print("Incorrect password.")
else:
    print("User not found.")
