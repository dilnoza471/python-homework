import sqlite3

# SQL Statements
CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS Books(
    Title TEXT, 
    Author TEXT, 
    Year_Published INTEGER, 
    Genre TEXT
)
"""

INSERT_BOOK = "INSERT INTO Books VALUES (?, ?, ?, ?)"

UPDATE_YEAR = "UPDATE Books SET Year_Published = ? WHERE Title = ?"

DELETE_OLD_BOOKS = "DELETE FROM Books WHERE Year_Published < 1950"

SELECT_BY_GENRE = "SELECT * FROM Books WHERE Genre = ?"

ADD_COLUMN_RATING = "ALTER TABLE Books ADD COLUMN Rating FLOAT"

UPDATE_RATING = "UPDATE Books SET Rating = ? WHERE Title = ?"

ORDERED_BOOKS = "SELECT * FROM Books ORDER BY Year_Published"

# Sample Data
books = [
    ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
    ('1984', 'George Orwell', 1949, 'Dystopian'),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')
]

ratings = {
    "To Kill a Mockingbird": 4.8,
    "1984": 4.7,
    "The Great Gatsby": 4.5
}

try:
    with sqlite3.connect("library.db") as con:
        cursor = con.cursor()

        # Create table
        cursor.execute(CREATE_TABLE)

        # Insert data (avoiding duplicates)
        cursor.executemany(INSERT_BOOK, books)

        # Update a book's publication year
        cursor.execute(UPDATE_YEAR, (1950, '1984'))

        # Query books by genre
        print("\nDystopian Books:")
        dystopian_books = cursor.execute(SELECT_BY_GENRE, ('Dystopian',)).fetchall()
        for book in dystopian_books:
            print(book)

        # Delete books published before 1950
        cursor.execute(DELETE_OLD_BOOKS)

        # Add a new column for ratings (Only if it doesn’t exist)
        try:
            cursor.execute(ADD_COLUMN_RATING)
        except sqlite3.OperationalError:
            pass  # Column already exists

        # Update ratings
        for title, rating in ratings.items():
            cursor.execute(UPDATE_RATING, (rating, title))

        # Retrieve and display all books ordered by publication year
        print("\nBooks Ordered by Year:")
        for book in cursor.execute(ORDERED_BOOKS).fetchall():
            print(book)

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    print("\nDatabase operations completed!")
