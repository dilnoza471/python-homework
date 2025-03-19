import uuid


class Book:
    def __init__(self, title, author):
        self.book_id = str(uuid.uuid4())[:6]  #get unique 6 char id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __repr__(self):
        """string representation"""
        return f"{self.book_id}| Title: {self.title}, Author: {self.author}, Borrowed: {self.is_borrowed}"

    def borrowed(self):
        """borrowed status"""
        self.is_borrowed = True

    def returned(self):
        """returned status"""
        self.is_borrowed = False
