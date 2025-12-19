# expense_tracker_gui.py

import tkinter as tk
from tkinter import messagebox
import csv

FILE_NAME = "expenses.csv"

def add_expense():
    date = date_entry.get()
    category = category_entry.get()
    amount = amount_entry.get()

    if date == "" or category == "" or amount == "":
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number")
        return

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount])

    messagebox.showinfo("Success", "Expense added")
    clear_fields()

def view_expenses():
    display.delete(1.0, tk.END)
    total = 0

    try:
        with open(FILE_NAME, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                display.insert(tk.END, f"{row[0]} | {row[1]} | ₹{row[2]}\n")
                total += float(row[2])
        display.insert(tk.END, f"\nTotal Expense: ₹{total}")
    except FileNotFoundError:
        display.insert(tk.END, "No expenses found")

def clear_fields():
    date_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("500x500")

tk.Label(root, text="Expense Tracker", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Date").grid(row=0, column=0, padx=5, pady=5)
date_entry = tk.Entry(frame)
date_entry.grid(row=0, column=1)

tk.Label(frame, text="Category").grid(row=1, column=0, padx=5, pady=5)
category_entry = tk.Entry(frame)
category_entry.grid(row=1, column=1)

tk.Label(frame, text="Amount").grid(row=2, column=0, padx=5, pady=5)
amount_entry = tk.Entry(frame)
amount_entry.grid(row=2, column=1)

tk.Button(root, text="Add Expense", width=20, command=add_expense).pack(pady=5)
tk.Button(root, text="View Expenses", width=20, command=view_expenses).pack(pady=5)

display = tk.Text(root, height=12, width=55)
display.pack(pady=10)

root.mainloop()
