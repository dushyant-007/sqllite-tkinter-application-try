import tkinter as tk
import sqlite3

def add_student():
  name = name_entry.get()
  age = age_entry.get()

  # Insert the student data into the database
  cur.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
  conn.commit()

def delete_student():
  name = name_entry.get()

  # Delete the student from the database
  cur.execute("DELETE FROM students WHERE name = ?", (name,))
  conn.commit()

def update_student():
  name = name_entry.get()
  age = age_entry.get()

  # Update the student's data in the database
  cur.execute("UPDATE students SET age = ? WHERE name = ?", (age, name))
  conn.commit()

# Create the database connection
conn = sqlite3.connect("class_database.db")

# Create the table
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, age INTEGER)")

# Create the UI
root = tk.Tk()

# Create the label
label = tk.Label(root, text="Student Information")
label.pack()

# Create the entry fields
name_entry = tk.Entry(root)
age_entry = tk.Entry(root)

# Create the buttons
add_button = tk.Button(root, text="Add Student", command=add_student)
delete_button = tk.Button(root, text="Delete Student", command=delete_student)
update_button = tk.Button(root, text="Update Student", command=update_student)

# Pack the entry fields and buttons
name_entry.pack()
age_entry.pack()
add_button.pack()
delete_button.pack()
update_button.pack()

# Create the mainloop
root.mainloop()

