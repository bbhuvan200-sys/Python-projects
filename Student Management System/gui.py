# student_management_gui.py

import tkinter as tk
from tkinter import messagebox

FILE_NAME = "students.txt"

def add_student():
    roll = roll_entry.get()
    name = name_entry.get()
    marks = marks_entry.get()

    if roll == "" or name == "" or marks == "":
        messagebox.showerror("Error", "All fields are required")
        return

    with open(FILE_NAME, "a") as f:
        f.write(f"{roll},{name},{marks}\n")

    messagebox.showinfo("Success", "Student added successfully")
    clear_fields()

def view_students():
    display.delete(1.0, tk.END)
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                roll, name, marks = line.strip().split(",")
                display.insert(tk.END, f"Roll: {roll} | Name: {name} | Marks: {marks}\n")
    except FileNotFoundError:
        display.insert(tk.END, "No records found")

def search_student():
    search_roll = roll_entry.get()
    display.delete(1.0, tk.END)
    found = False

    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                roll, name, marks = line.strip().split(",")
                if roll == search_roll:
                    display.insert(tk.END, f"Found → Roll: {roll} | Name: {name} | Marks: {marks}")
                    found = True
                    break
        if not found:
            display.insert(tk.END, "Student not found")
    except FileNotFoundError:
        display.insert(tk.END, "No records found")

def clear_fields():
    roll_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Student Management System")
root.geometry("500x500")

tk.Label(root, text="Student Management System", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Roll No").grid(row=0, column=0, padx=5, pady=5)
roll_entry = tk.Entry(frame)
roll_entry.grid(row=0, column=1)

tk.Label(frame, text="Name").grid(row=1, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame)
name_entry.grid(row=1, column=1)

tk.Label(frame, text="Marks").grid(row=2, column=0, padx=5, pady=5)
marks_entry = tk.Entry(frame)
marks_entry.grid(row=2, column=1)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Student", width=15, command=add_student).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="View Students", width=15, command=view_students).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Search Student", width=15, command=search_student).grid(row=0, column=2, padx=5)

display = tk.Text(root, height=10, width=55)
display.pack(pady=10)

root.mainloop()
