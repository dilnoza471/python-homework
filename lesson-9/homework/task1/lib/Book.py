import uuid


class Book:
    def __init__(self, title, author):
        self.book_id = str(uuid.uuid4())[:6]
        self.title = title
        self.author = author
        self.is_borrowed = False
    def __repr__(self):
        return f"{self.book_id}| Title: {self.title}, Author: {self.author}, Borrowed: {self.is_borrowed}"

    def borrowed(self):
        self.is_borrowed = True
    def returned(self):
        self.is_borrowed = False