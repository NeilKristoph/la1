print("===== Temperature Checker =====")
temp = int(input("Enter your current temperature: "))
if temp > 30:
    print("Hot day! Stay hydrated.")
elif temp < 31 and temp > 9:
    print("Pleasant weather!")
else:
    print("Cold day!")
