from Project.Logic.library_logic import Library
from Project.Models.Book import Book, Status_book
from Project.Models.User import User


def test_add_book(): #to add a book
    lib = Library()
    b = Book(1, "Pride and Prejudice", "Jane Austen")
    lib.add_book(b)
    assert 1 in lib.books

def test_add_book_duplicate(): #to add a book that already exists
    lib = Library()
    b = Book(1, "Pride and Prejudice", "Jane Austen")
    lib.add_book(b)
    try:
        lib.add_book(b)
        assert False
    except ValueError:
        assert True #we're supposed to have a ValueError

def test_remove_book(): #to remove a book
    lib = Library()
    b = Book(1, "Pride and Prejudice", "Jane Austen")
    lib.add_book(b)
    lib.remove_book(1)
    assert 1 not in lib.books

def test_remove_book_borrowed(): #to remove a book that is currently borrowed
    lib = Library()
    lib.add_book(Book(1, "Pride and Prejudice", "Jane Austen", status=Status_book.borrowed))
    try:
        lib.remove_book(1)
        assert False
    except ValueError:
        assert True

def test_books_list(): # to list all books in the library
    lib = Library()
    lib.add_book(Book(1, "Pride and Prejudice", "Jane Austen"))
    lib.add_book(Book(2,"To Kill a Mockingbird","Harper Lee"))
    lst = lib.books_list()
    assert len(lst) == 2

def test_available_books_list(): # to list available books in the library
    lib = Library()
    lib.add_book(Book(1, "Pride and Prejudice", "Jane Austen"))
    lib.add_book(Book(2,"To Kill a Mockingbird","Harper Lee", status=Status_book.borrowed))
    available = lib.available_books_list()
    assert len(available) == 1

def test_search_books_title(): # search by title
    lib = Library()
    lib.add_book(Book(1, "Harry Potter", "JKR"))
    lib.add_book(Book(2, "The Stainless Steel Rat", "Harry Harrison" ))
    res = lib.search_books(title="harry")
    assert len(res) == 1

def test_search_books_author():  # search by author
    lib = Library()
    lib.add_book(Book(1, "Pride and Prejudice", "Jane Austen"))
    lib.add_book(Book(2, "Emma", "Jane Austen"))
    lib.add_book(Book(3, "Jane Eyre", "Charlotte Brontë"))
    res = lib.search_books(author="Jane")
    assert len(res) == 2

def test_search_books_keyword(): # search by keyword
    lib = Library()
    lib.add_book(Book(1, "Pride and Prejudice", "Jane Austen"))
    lib.add_book(Book(2, "Emma", "Jane Austen"))
    lib.add_book(Book(3, "Jane Eyre", "Charlotte Brontë"))
    lib.add_book(Book(4, "Harry Potter", "JKR"))
    lib.add_book(Book(5, "The Stainless Steel Rat", "Harry Harrison"))
    res = lib.search_books(keyword="Jane")
    assert len(res) == 3
    res = lib.search_books(keyword="Harry")
    assert len(res) == 2

def test_create_user(): #to create a new user
    lib = Library()
    u = User(17, "Alicia")
    lib.create_user(u)
    assert 17 in lib.users
    assert u.borrowed_books == []

def test_create_user_duplicate(): #to create a user that already exists
    lib = Library()
    u = User(17, "Alice")
    lib.create_user(u)
    try:
        lib.create_user(u)
        assert False
    except ValueError: #Should raise a ValueError
        assert True

def test_remove_user(): #to remove a user
    lib = Library()
    u = User(17, "Alicia")
    lib.create_user(u)
    lib.remove_user(17)
    assert 17 not in lib.users

def test_remove_nonexisting_user(): #to remove a non-existing user
    lib = Library()
    u = User(17, "Alicia")
    lib.create_user(u)
    try:
        lib.remove_user(3)
        assert False
    except ValueError:
        assert True

def test_remove_user_with_books(): #to remove a user with borrowed books
    lib = Library()
    u = User(17, "Alicia", borrowed_books=[1])
    lib.create_user(u)
    try:
        lib.remove_user(17)
        assert False
    except ValueError:
        assert True

def test_users_list(): # to list all users
    lib = Library()
    lib.create_user(User(1, "Alicia"))
    lib.create_user(User(2, "Mahdi"))
    lst = lib.users_list()
    assert len(lst) == 2


def test_loan_book(): #to loan a book
    lib = Library()
    lib.create_user(User(17, "Alicia"))
    lib.add_book(Book(3, "Pride and Prejudice", "Jane Austen"))
    lib.loan_book(17, 3)
    assert lib.books[3].status == Status_book.borrowed
    assert 3 in lib.users[17].borrowed_books

def test_loan_nonexisting_book(): #to loan a book that doesn't exist
    lib = Library()
    lib.create_user(User(17, "Alicia"))
    try:
        lib.loan_book(17, 1)
        assert False
    except ValueError:
        assert True

def test_loan_nonexisting_user(): #to loan to a user that doesn't exist
    lib = Library()
    lib.add_book(Book(3, "Pride and Prejudice", "Jane Austen"))
    try:
        lib.loan_book(17, 3)
        assert False
    except ValueError:
        assert True

def test_loan_borrowed_book(): #to loan a book that is already borrowed
    lib = Library()
    lib.add_book(Book(3, "Pride and Prejudice", "Jane Austen", status=Status_book.borrowed))
    lib.create_user(User(17, "Alicia"))
    try:
        lib.loan_book(17, 3)
        assert False
    except ValueError:
        assert True #you can't borrow a book that is already borrowed


def test_return_book(): #to return a book
    lib = Library()
    lib.add_book(Book(3, "Pride and Prejudice", "Jane Austen"))
    lib.create_user(User(17, "Alicia"))
    lib.loan_book(17, 3)
    lib.return_book(17, 3)
    assert lib.books[3].status == Status_book.available
    assert 3 not in lib.users[17].borrowed_books

def test_return_book_nonexisting_user(): #to return a book for a user that doesn't exist
    lib = Library()
    lib.add_book(Book(2, "Emma", "Jane Austen", status=Status_book.borrowed))
    lib.add_book(Book(3, "Pride and Prejudice", "Jane Austen", status=Status_book.borrowed))
    lib.create_user(User(17, "Alicia", borrowed_books=[3]))
    try:
        lib.return_book(10, 2)
        assert False
    except ValueError:
        assert True #the user does not exist

def test_return_book_nonexisting_book(): #to return a book that doesn't exist
    lib = Library()
    lib.add_book(Book(3, "Pride and Prejudice", "Jane Austen", status=Status_book.borrowed))
    lib.create_user(User(17, "Alicia", borrowed_books=[3]))
    try:
        lib.return_book(17, 1)
        assert False
    except ValueError:
        assert True #the book does not exist

def test_return_book_not_borrowed_by_the_user(): #to return a book that was not borrowed by this user
    lib = Library()
    lib.add_book(Book(2, "Emma", "Jane Austen", status=Status_book.borrowed))
    lib.add_book(Book(3, "Pride and Prejudice", "Jane Austen", status=Status_book.borrowed))
    lib.create_user(User(17, "Alicia", borrowed_books=[3]))
    try:
        lib.return_book(17, 2)
        assert False
    except ValueError:
        assert True #the book hasn't been borrowed by the same user

def test_statistics():
    lib = Library()
    lib.add_book(Book(1, "Pride and Prejudice", "Jane Austen"))
    lib.add_book(Book(2, "Emma", "Jane Austen"))
    lib.add_book(Book(3, "Jane Eyre", "Charlotte Brontë"))
    lib.add_book(Book(4, "Harry Potter", "JKR"))
    lib.add_book(Book(5, "The Stainless Steel Rat", "Harry Harrison"))
    lib.add_book(Book(6, "Moby-Dick", "Herman Melville"))
    lib.create_user(User(1,"Alicia", borrowed_books=[1,2,3]))
    lib.create_user(User(2,"Mahdi"))
    lib.create_user(User(3,"Lina", borrowed_books= [4]))
    lib.create_user(User(4,"Amal"))
    lib.create_user(User(5,"Mohamed", borrowed_books=[5,6]))

    stats = lib.statistics()
    assert stats["Number of books"] == 6
    assert stats["Number of users"] == 5
    assert stats["Borrowed books distribution"][5] == 2
    assert stats["Borrowed books distribution"][2] == 0
