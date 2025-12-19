# expense_tracker.py

import csv

FILE_NAME = "expenses.csv"

def add_expense():
    date = input("Enter Date (DD/MM/YYYY): ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount])

    print("Expense added successfully!")

def view_expenses():
    total = 0
    try:
        with open(FILE_NAME, "r") as f:
            reader = csv.reader(f)
            print("\nDate | Category | Amount")
            print("-" * 30)
            for row in reader:
                print(f"{row[0]} | {row[1]} | {row[2]}")
                total += float(row[2])
        print("\nTotal Expense:", total)
    except FileNotFoundError:
        print("No expenses found.")

def main():
    while True:
        print("\n1.Add Expense\n2.View Expenses\n3.Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

main()
