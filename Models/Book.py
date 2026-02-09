from dataclasses import dataclass
from enum import Enum

class Status_book(Enum):
    """
Enumeration representing the status of a book.
Values:
        available: The book is available for borrowing.
        borrowed: The book is currently borrowed by a user.
    """
    available = "available"
    borrowed = "borrowed"
    def __str__(self) -> str:
        return self.value

@dataclass
class Book:
    """
    Represents a book in the library.

    Attributes:
    - id_book (int): Unique identifier of the book.
    - title (str): Title of the book.
    - author (str): Author of the book.
    - status (Status_book): Current status of the book (available or borrowed).
    """
    id_book: int
    title: str
    author: str
    status: Status_book = Status_book.available #by default

# status:
    def is_available(self) -> bool: #pour verifier
        return self.status == Status_book.available
    def set_available(self) -> None:
        self.status = Status_book.available
    def set_borrowed(self) -> None:
        self.status = Status_book.borrowed

# Visualisation
    def __str__(self):
        return f"[{self.id_book}] {self.title} - {self.author} : {self.status}"

