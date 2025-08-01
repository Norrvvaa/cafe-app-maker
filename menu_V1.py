import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Item Manager")
root.geometry("300x400")

# Functions
def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter an item.")

def remove_item():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
    else:
        messagebox.showwarning("Selection Error", "Please select an item to remove.")

# Entry box
entry = tk.Entry(root, width=25)
entry.pack(pady=10)

# Add Button
add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.pack(pady=5)

# Listbox to show items
listbox = tk.Listbox(root, width=30, height=15)
listbox.pack(pady=10)

# Remove Button
remove_button = tk.Button(root, text="Remove Selected", command=remove_item)
remove_button.pack(pady=5)

# Run the application
root.mainloop()
