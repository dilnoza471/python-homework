import uuid


class Member:
    def __init__(self, name):
        self.member_id = str(uuid.uuid4())[:6]  #to uniquely identify a member
        self.name = name
        self.borrowed_books = []  #max should be 3

    def borrow_book(self, book):
        """borrow a book"""
        self.borrowed_books.append(book)

    def return_book(self, book):
        """return a book"""
        self.borrowed_books.remove(book)

    def search_book(self, book_id):
        """search book by id inside borrowed books"""
        for book in self.borrowed_books:
            if book.book_id == book_id:
                return book
        return None

    def __repr__(self):
        """string representation"""
        return f"{self.member_id} | Member({self.name})"

    def show(self):
        """info about the member + borrowed books"""
        print(f"{self.member_id} | Member({self.name})")

        if len(self.borrowed_books) == 0:
            print("No borrowed books")
        else:
            print("Borrowed books:")
            for i in self.borrowed_books:
                print(i)
