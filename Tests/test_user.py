from Project.Models.User import User

def test_add_borrowed_book(): #to add a book to the user's borrowed books
    u = User(17, "Alicia")
    u.add_borrowed_book(3)
    assert u.borrowed_books == [3]

def test_remove_borrowed_book(): #to remove a book from the user's borrowed books
    u = User(17, "Alicia", borrowed_books=[1, 2])
    u.remove_borrowed_book(1)
    assert u.borrowed_books == [2]

