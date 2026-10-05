# Project: Expense Tracker | Installment 2
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

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print()
print("-" * 40)
print("SUMMARY")
print(f"{'':>2}{f'- {item1}:':<17}${amount1}")
print(f"{'':>2}{f'- {item2}:':<17}${amount2}")
print(f"{'Total spent:':<19}${total}")
print(f"{'Average:':<19}${average}")
print("-" * 40)

print(f"Made by: Marsha Lei Hernandez | Installment 2")