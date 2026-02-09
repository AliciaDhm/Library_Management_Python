from dataclasses import dataclass, field
from typing import List

@dataclass
class User:
    """
Represents a user registered in the library.
Attributes:
    - id_user (int): Unique identifier of the user.
    - user_name (str): Name of the user.
    - borrowed_books (List[int]): IDs of the books borrowed by the user.
    """
    id_user: int
    user_name: str
    borrowed_books: List[int] = field(default_factory=list)

    def add_borrowed_book(self, id_book: int)-> None:
        if id_book not in self.borrowed_books: #to avoid having duplicates
            self.borrowed_books.append(id_book)
    def remove_borrowed_book(self, id_book: int)-> None:
        if id_book in self.borrowed_books:
            self.borrowed_books.remove(id_book)

    # Visualisation
    def __str__(self) -> str:
        return f"[{self.id_user}] {self.user_name} : ({self.borrowed_books})"