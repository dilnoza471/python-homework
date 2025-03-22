import sqlite3

# SQL Statements
CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT, 
    Species TEXT, 
    Age INTEGER
)
"""

INSERT_DATA = "INSERT INTO Roster VALUES (?, ?, ?)"

UPDATE_NAME = "UPDATE Roster SET Name = ? WHERE Name = ?"

SELECT_BAJORAN = "SELECT * FROM Roster WHERE Species = 'Bajoran'"

DELETE_OLD = "DELETE FROM Roster WHERE Age > 100"

ORDER_BY_AGE = "SELECT * FROM Roster ORDER BY Age DESC"

# Data
roster_data = [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
]

try:
    with sqlite3.connect("roster.db") as connection:
        cursor = connection.cursor()

        # Create table
        cursor.execute(CREATE_TABLE)

        # Insert data (avoiding duplicates)
        cursor.executemany(INSERT_DATA, roster_data)

        # Update data
        cursor.execute(UPDATE_NAME, ('Ezri Dax', 'Jadzia Dax'))

        # Fetch Bajoran characters
        print("\nBajoran Characters:")
        for row in cursor.execute(SELECT_BAJORAN).fetchall():
            print(row)

        # Delete old characters
        cursor.execute(DELETE_OLD)

        # Display sorted roster by Age (Descending)
        print("\nRoster (Sorted by Age):")
        for row in cursor.execute(ORDER_BY_AGE).fetchall():
            print(row)

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    print("\nDatabase operations completed!")
