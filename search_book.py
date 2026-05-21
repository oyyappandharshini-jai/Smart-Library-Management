from database import cursor


def search_book(title_entry, tree):

    keyword = title_entry.get()

    for item in tree.get_children():
        tree.delete(item)

    cursor.execute(
        "SELECT * FROM books WHERE title LIKE ?",
        ('%' + keyword + '%',)
    )

    rows = cursor.fetchall()

    for row in rows:
        tree.insert('', 'end', values=row)