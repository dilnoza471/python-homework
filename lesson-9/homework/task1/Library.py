from lib import *


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print("New book added.")
        print(self.books[-1])

    def add_member(self, member):
        self.members.append(member)
        print("New member added.")
        print(self.members[-1])

    def search_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        raise BookNotFoundException

    def search_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        raise MemberNotFoundException
    def return_books(self, book_id, member_id):
        book = self.search_book(book_id)
        member = self.search_member(member_id)
        if book.is_borrowed and member.search_book(book.book_id):
            book.returned()
            member.return_book(book)
            print("Book returned.")
        else:
            print("Member already returned the book")
    def borrow_books(self, book_id, member_id):
        book = self.search_book(book_id)
        member = self.search_member(member_id)
        if book.is_borrowed:
            raise BookAlreadyBorrowedException
        if len(member.borrowed_books) == 3:
            raise MemberLimitExceededException
        book.borrowed()
        member.borrow_book(book)
        print("Member borrowed the book. ")

    def show_members(self):
        for member in self.members:
            print(member)
    def show_books(self):
        for book in self.books:
            print(book)

def show_menu():
    print("""
    1. Add book
    2. Add member
    3. Return book
    4. Borrow book
    5. Show members
    6. Show books
    7. Search Member
    8. Exit""")
def main():
    library = Library()
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(Book(title, author))
        elif choice == "2":
            name = input("Enter member's name: ")
            library.add_member(Member(name))
        elif choice == "3":
            book_id = input("Enter book id: ")
            mem_id = input("Enter member id: ")
            try:
                library.return_books(book_id, mem_id)
            except BookNotFoundException as e:
                print(e)
            except MemberNotFoundException as e:
                print(e)
        elif choice == "4":
            book_id = input("Enter book id: ")
            mem_id = input("Enter member id: ")
            try:
                library.borrow_books(book_id, mem_id)
            except Exceptions.BookNotFoundException as e:
                print(e)
            except MemberNotFoundException as e:
                print(e)
            except MemberLimitExceededException as e:
                print(e)
            except BookAlreadyBorrowedException as e:
                print(e)
        elif choice == "5":
            library.show_members()
        elif choice == "6":
            library.show_books()
        elif choice == "7":
            try:
                member = library.search_member(input("Enter member id: "))
            except MemberNotFoundException as e:
                print(e)
            else:
                member.show()
        elif choice == "8":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

