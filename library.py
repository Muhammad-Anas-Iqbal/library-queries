import sqlite3

conn = sqlite3.connect("library.db")
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS books;

CREATE TABLE books (
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    price INTEGER,
    stock INTEGER
);

INSERT INTO books VALUES
(1, 'The Great Gatsby', 'Fiction', 1200, 3),
(2, '1984', 'Fiction', 950, 7),
(3, 'Python Basics', 'Technology', 1500, 10),
(4, 'Clean Code', 'Technology', 1800, 4),
(5, 'The Alchemist', 'Fiction', 1100, 2),
(6, 'Harry Potter', 'Fantasy', 1300, 6),
(7, 'Data Science Handbook', 'Technology', 2200, 3),
(8, 'Pride and Prejudice', 'Fiction', 800, 4);
""")

conn.commit()

print("Database created.\n\nBooks with price greater than 1000:\n")

cur.execute("""
SELECT title, price
FROM books
WHERE price > 1000
ORDER BY price DESC;
""")

for row in cur.fetchall():
    print(row)

print("\n\nAll books in the library:\n")

cur.execute("""
SELECT title AS book_title, price
FROM books;
""")

for row in cur.fetchall():
    print(row)

print("\n\nFiction books with stock less than 5:\n")

cur.execute("""
SELECT *
FROM books
WHERE genre = 'Fiction' AND stock < 5;
""")

for row in cur.fetchall():
    print(row)


conn.close()