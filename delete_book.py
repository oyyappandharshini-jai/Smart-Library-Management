from tkinter import messagebox
from database import conn, cursor, show_books


def delete_book(tree):

    selected = tree.selection()

    if not selected:
        messagebox.showerror("Error", "Select a book first")
        return

    item = tree.item(selected)

    book_id = item['values'][0]

    cursor.execute(
        "DELETE FROM books WHERE id=?",
        (book_id,)
    )

    conn.commit()

    messagebox.showinfo("Deleted", "Book Deleted Successfully")

    show_books(tree)