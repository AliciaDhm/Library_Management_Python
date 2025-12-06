from typing import Dict, List, Optional
from Project.Models.Book import Book
from Project.Models.User import User
import matplotlib.pyplot as plt


class Library:
    """
    Manages the core operations of the library system:
      - add/remove books and users,
      - search for books,
      - handle borrowing and returning books,
      - statistics on library activity.

    """

    def __init__(self) -> None:
        self.books: Dict[int, Book] = {}
        self.users: Dict[int, User] = {}

    # I.book management

    #Add book
    def add_book(self, book: Book) -> None:
        """
    Adds a book to the library
    Parameters:
        book (Book): The book to add
    Raises:
        ValueError: If a book with the same ID already exists
        """
        if book.id_book in self.books:
            raise ValueError(f"The book {book.id_book} is already in the library")
        self.books[book.id_book] = book

    #Remove book
    def remove_book(self, id_book: int) -> None:
        """
    Removes a book from the library
    Parameters:
        id_book (int): The ID of the book to remove
    Raises:
        ValueError: If The book does not exist in the library
                    or if the book is currently borrowed
        """
        if id_book not in self.books: #to ensure that the book exists
            raise ValueError(f"The book {id_book} is not in the library")

        book = self.books[id_book]
        if not book.is_available(): #to ensure that the book isn't already borrowed
                raise ValueError(f"The book {id_book} is borrowed from the library and cannot be removed")

        del self.books[id_book]

    #List books
    def books_list(self) -> List[Book]:
        return list(self.books.values())

    #List of available books
    def available_books_list(self) -> List[Book]:
        available_books_list = []
        for book in self.books.values():
            if book.is_available():
                available_books_list.append(book)
        return available_books_list

    #search for a book
    def search_books(
            self,
            title: Optional[str] = None,
            author: Optional[str] = None,
            keyword: Optional[str] = None
                    ) -> List[Book]:
        """
    Searches for books in the library.
    Parameters:
        title (str, optional): Title (or a part of it) to search for.
        author (str, optional): Author name (or a part of it) to search for.
        keyword (str, optional): Keyword to search in title or author.
    Returns:
        List[Book]: A list of books matching the search criteria.
        """
        results= list(self.books.values())
        if title is not None:
            txt = title.lower()
            results = [book for book in results if txt in book.title.lower()]
        if author is not None:
            txt = author.lower()
            results = [book for book in results if txt in book.author.lower()]
        if keyword is not None:
            txt = keyword.lower()
            results= [book for book in results if txt in book.title.lower() or txt in book.author.lower()]
        return results


    # II. Users management
    #create users
    def create_user(self, user: User) -> None:
        """
    Registers a new user in the library.
    Parameters:
        user (User): The user to add.
    Raises:
        ValueError: If a user with the same ID already exists.
        """
        if user.id_user in self.users:
            raise ValueError(f"The user {user.id_user} has already been created")
        self.users[user.id_user] = user

    #remove users
    def remove_user(self, id_user: int) -> None:
        """
        Removes a user from the library
        Parameters:
            id_user (int): The ID of the user to remove
        Raises:
            ValueError: If the user does not exist in the library
                        or if the user has borrowed books
        """
        if id_user not in self.users:
            raise ValueError(f"The user {id_user} is not registered")
        user = self.users[id_user]
        if user.borrowed_books:
            raise ValueError(f"The user {user.id_user} cannot be removed due to borrowed books")
        del self.users[id_user]

    #list registered users
    def users_list(self) -> List[User]:
        return list(self.users.values())


    # III. Loan and Return Management
    #loan
    def loan_book(self, id_user: int, id_book: int) -> None:
        """
    Loans a book to a user.
    Parameters:
        id_user (int): ID of the user requesting the book.
        id_book (int): ID of the book to borrow.
    Raises:
        ValueError: If the user does not exist,
                    if the book does not exist,
                    or if the book is already borrowed.

        """
        if id_user not in self.users:
            raise ValueError(f"The ID user : {id_user} does not exist.")
        if id_book not in self.books:
            raise ValueError(f"The ID book : {id_book} does not exist in the library")

        book = self.books[id_book]
        user = self.users[id_user]

        if not book.is_available():
            raise ValueError(f"The ID book : {id_book} is not available, it has been borrowed")

        book.set_borrowed()
        user.add_borrowed_book(id_book)

    #return
    def return_book(self, id_user: int, id_book: int) -> None:
        """
    Returns a borrowed book to the library.
    Parameters:
        id_user (int): ID of the user returning the book.
        id_book (int): ID of the book to return.
    Raises:
        ValueError: If the user does not exist,
                    if the book does not exist,
                    if the book was not borrowed,
                    or if the book was not borrowed by this user.
        """
        if id_user not in self.users:
            raise ValueError(f"The ID user : {id_user} does not exist.")
        if id_book not in self.books:
            raise ValueError(f"The ID book : {id_book} does not exist in the library")

        book = self.books[id_book]
        user = self.users[id_user]

        if book.is_available():
            raise ValueError(f"The ID book : {id_book} it has not been borrowed")
        if id_book not in user.borrowed_books:
            raise ValueError(f"The ID book : {book.id_book} has not been borrowed by : {user.id_user}")

        book.set_available()
        user.remove_borrowed_book(id_book)


    # IV. Statistics:
    def statistics(self) -> dict:
        nb_tot_books = len(self.books)
        nb_tot_users = len(self.users)

        borrow_dist = {}
        for user in self.users.values():
            borrow_dist[user.id_user] = len(user.borrowed_books)

        return {
                    "Number of books": nb_tot_books,
                    "Number of users": nb_tot_users,
                    "Borrowed books distribution": borrow_dist
                }

    def plot_borrow_dist(self) -> None:
        stats = self.statistics()
        borrow_dist = stats["Borrowed books distribution"]


        user_ids = list(borrow_dist.keys())
        nb_books = list(borrow_dist.values())

        labels = []
        for user_id in user_ids:
            name = self.users[user_id].user_name
            labels.append(name)

        plt.figure()
        plt.bar(labels, nb_books)
        plt.plot(labels, nb_books, marker='o')
        plt.xlabel("Users")
        plt.ylabel("Number of borrowed books")
        plt.title("Distribution of borrowed books per user")
        plt.tight_layout()
        plt.show()
