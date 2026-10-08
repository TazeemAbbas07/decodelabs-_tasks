total = 0

while True:
    expense = float(input("Enter expense amount: "))

    total += expense

    print("Total Spent:", total)

    choice = input("Do You want to Add another expense? (yes/no): ")

    if choice.lower() == "no":
        break