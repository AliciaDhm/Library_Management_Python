from Project.Models.Book import Book, Status_book

def test_book_is_available():
    b = Book(1, "Pride and Prejudice", "Jane Austen")
    assert b.is_available() is True

def test_book_set_borrowed():
    b = Book(1, "Pride and Prejudice", "Jane Austen")
    b.set_borrowed()
    assert b.status == Status_book.borrowed
    assert b.is_available() is False

def test_book_set_available():
    b = Book(1, "Pride and Prejudice", "Jane Austen", status=Status_book.borrowed)
    b.set_available()
    assert b.status == Status_book.available
    assert b.is_available() is True

def test_book_str():
    b = Book(1, "Pride and Prejudice", "Jane Austen")
    assert "[1] Pride and Prejudice - Jane Austen :" in str(b)

