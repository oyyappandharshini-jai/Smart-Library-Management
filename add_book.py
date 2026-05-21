from tkinter import messagebox
from database import conn, cursor, show_books


def add_book(title_entry,author_entry,quantity_entry,tree):

    title = title_entry.get()
    author = author_entry.get()
    quantity = quantity_entry.get()

    if title == "" or author == "" or quantity == "":
        messagebox.showerror("Error", "All fields are required")
        return

    cursor.execute(
        "INSERT INTO books(title, author, quantity) VALUES(?,?,?)",
        (title, author, quantity)
    )

    conn.commit()

    messagebox.showinfo("Success", "Book Added Successfully")

    title_entry.delete(0, 'end')
    author_entry.delete(0, 'end')
    quantity_entry.delete(0, 'end')

    show_books(tree)