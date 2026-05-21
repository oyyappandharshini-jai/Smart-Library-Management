import tkinter as tk
from tkinter import ttk
from add_book import add_book
from search_book import search_book
from delete_book import delete_book
from database import create_table, show_books

# Create Database Table
create_table()

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Smart Library Management System")
root.geometry("900x600")
root.config(bg="#f5f5f5")

# ---------------- TITLE ---------------- #

heading = tk.Label(
    root,
    text="SMART LIBRARY MANAGEMENT SYSTEM",
    font=("Arial", 22, "bold"),
    bg="#f5f5f5",
    fg="darkblue"
)

heading.pack(pady=10)

# ---------------- FORM FRAME ---------------- #

form_frame = tk.Frame(root, bg="#f5f5f5")
form_frame.pack(pady=10)

# Book Title

tk.Label(form_frame,
         text="Book Title:",
         font=("Arial", 12),
         bg="#f5f5f5").grid(row=0, column=0, padx=10, pady=5)

book_title = tk.Entry(form_frame, width=30, font=("Arial", 12))
book_title.grid(row=0, column=1)

# Author

tk.Label(form_frame,
         text="Author:",
         font=("Arial", 12),
         bg="#f5f5f5").grid(row=1, column=0, padx=10, pady=5)

book_author = tk.Entry(form_frame, width=30, font=("Arial", 12))
book_author.grid(row=1, column=1)

# Quantity

tk.Label(form_frame,
         text="Quantity:",
         font=("Arial", 12),
         bg="#f5f5f5").grid(row=2, column=0, padx=10, pady=5)

book_quantity = tk.Entry(form_frame, width=30, font=("Arial", 12))
book_quantity.grid(row=2, column=1)

# ---------------- TABLE ---------------- #

columns = ("ID", "Title", "Author", "Quantity")

book_table = ttk.Treeview(root,
                          columns=columns,
                          show="headings",
                          height=12)

for col in columns:
    book_table.heading(col, text=col)
    book_table.column(col, width=180)

book_table.pack(pady=20)

# Show books initially
show_books(book_table)

# ---------------- BUTTONS ---------------- #

button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=10)

add_btn = tk.Button(
    button_frame,
    text="Add Book",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    width=15,
    command=lambda: add_book(book_title,
                             book_author,
                             book_quantity,
                             book_table)
)

add_btn.grid(row=0, column=0, padx=10)

search_btn = tk.Button(
    button_frame,
    text="Search Book",
    font=("Arial", 12, "bold"),
    bg="orange",
    fg="white",
    width=15,
    command=lambda: search_book(book_title, book_table)
)

search_btn.grid(row=0, column=1, padx=10)


delete_btn = tk.Button(
    button_frame,
    text="Delete Book",
    font=("Arial", 12, "bold"),
    bg="red",
    fg="white",
    width=15,
    command=lambda: delete_book(book_table)
)


delete_btn.grid(row=0, column=2, padx=10)

show_btn = tk.Button(
    button_frame,
    text="Show Books",
    font=("Arial", 12, "bold"),
    bg="blue",
    fg="white",
    width=15,
    command=lambda: show_books(book_table)
)

show_btn.grid(row=0, column=3, padx=10)

# ---------------- RUN ---------------- #

root.mainloop()