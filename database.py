import sqlite3

# Database Connection

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create Table

def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        quantity INTEGER
    )
    """)

    conn.commit()

# Show Books

def show_books(tree):

    for item in tree.get_children():
        tree.delete(item)

    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert('', 'end', values=row)