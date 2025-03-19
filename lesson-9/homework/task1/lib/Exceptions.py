class BookNotFoundException(Exception):
    def __init__(self):
        self.msg = "Book not found"
        super().__init__(self.msg)


class BookAlreadyBorrowedException(Exception):
    def __init__(self):
        self.msg = "Book already borrowed"
        super().__init__(self.msg)


class MemberLimitExceededException(Exception):
    def __init__(self):
        self.msg = "Member limit exceeded"
        super().__init__(self.msg)


class MemberNotFoundException(Exception):
    def __init__(self):
        self.msg = "Member not found"
        super().__init__(self.msg)
