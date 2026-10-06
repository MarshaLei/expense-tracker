# Project: Expense Tracker | Installment 3
# Author: Marsha Lei Hernandez
# A simple landing page for a personal expense tracker.

print("=" * 40)
print(f"{'EXPENSE TRACKER':^40}")
print(f"{'Know where your money goes.':>35}")
print("=" * 40)

print("\nMAIN MENU")
print(f"{'[1]':>5} {'Add an expense':<26}(coming soon)")
print(f"{'[2]':>5} {'View all expenses':<26}(coming soon)")
print(f"{'[3]':>5} {'Show total spent':<26}(coming soon)")
print(f"{'[4]':>5} {'Exit':<26}(coming soon)")

name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

item1 = input("\nFirst expense? ")
amount1 = float(input("Amount? "))

subtotal = 0
subtotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

average = subtotal / 2

tax_percent = int(input("Tax rate %? "))
tax = subtotal * (tax_percent / 100)
total = subtotal + tax

budget = float(input("Your budget? "))
over_budget = total > budget 
left = budget - total 

print()
print("-" * 40)
print("SUMMARY")
print(f"{'':>2}{f'- {item1}:':<14}${amount1}")
print(f"{'':>2}{f'- {item2}:':<14}${amount2}")
print(f"{'Subtotal:':<16}${subtotal}")
print(f"{'Average:':<16}${average}")
print(f"{f'Tax ({tax_percent:.1f}%):':<16}${tax}")
print(f"{'Grand total:':<16}${total}")
print(f"{'Over budget?':<16}{over_budget}")
print(f"{'Left in budget:':<16}${left}")
print("-" * 40)

print(f"Made by: Marsha Lei Hernandez | Installment 3")