# Project: Expense Tracker | Installment 5
# Author: Marsha Lei Hernandez
# A simple landing page for a personal expense tracker.

print("=" * 40)
print(f"{'EXPENSE TRACKER':^40}")
print(f"{'Know where your money goes.':>35}")
print("=" * 40)

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

print(f"Welcome, {name}!")

subtotal = 0
count = 0
choice = ""

while choice != "4":
    print("\nMAIN MENU")
    print(f"{'[1]':>5} {'Add an expense'}")
    print(f"{'[2]':>5} {'View all expenses':<20}(coming soon)")
    print(f"{'[3]':>5} {'Show total spent'}")
    print(f"{'[4]':>5} {'Exit'}")

    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))

        subtotal += amount
        count += 1

        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")

    elif choice == "2":
        print(f"{'':>2}Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * tax_percent / 100
        total = subtotal + tax
        left = budget - total

        print(f"{'':>2}{'Expenses:':<14}{count}")
        print(f"{'':>2}{'Subtotal:':<14}${subtotal:.1f}")
        print(f"{'':>2}{f'Tax ({tax_percent:.1f}%):':<14}${tax:.1f}")
        print(f"{'':>2}{'Grand total:':<14}${total:.1f}")

        if total > budget:
            print(f"{'':>2}Over budget by ${abs(left):.1f}!")
        elif total > budget * 0.9:
            print(f"{'':>2}Careful: only ${left} left.")
        else:
            print(f"{'':>2}Within budget. ${left} left.")

    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("-" * 40)
        print("Made by: Marsha Lei Hernandez | Installment 5")
        print("=" * 40)
     
    else:
        print(f"{'':>2}Please choose 1, 2, 3 or 4.")