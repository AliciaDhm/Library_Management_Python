from Project.Logic.library_logic import Library
from Project.Models.Book import Book, Status_book
from Project.Models.User import User

def main():
    library = Library()
    print("Hello! Welcome to the Library!")

    while True:
        print(" What do you want to do? Choose the NUMBER of the task!")
        print(" 1 - List books")
        print(" 2 - List users")
        print(" 3 - List available books")
        print(" 4 - Add a book")
        print(" 5 - Add a user")
        print(" 6 - Remove a book")
        print(" 7 - Remove a user")
        print(" 8 - Search a book")
        print(" 9 - Borrow a book")
        print("10 - Return a book")
        print("11 - Show statistics")
        print("12 - Show The distribution plot")
        print(" 0 - Exit")


        commande = input(" The number of the choice: ").strip()

        match commande:

            case "1": #List books
                books = library.books_list()
                if not books:
                    print("No books in the library.")
                else:
                    for book in books:
                        status = "available" if book.is_available() else "borrowed"
                        print(f"[{book.id_book}] {book.title} - {book.author} ({status})")


            case "2": #List users
                users = library.users_list()
                if not users:
                    print("No users registered.")
                else:
                    for user in users:
                        print(f"[{user.id_user}] {user.user_name} - borrowed: {user.borrowed_books}")

            case "3": #List available books
                available_books = library.available_books_list()
                if not available_books:
                    print("No available books.")
                else:
                    print("Available books:")
                    for book in available_books:
                        print(f"[{book.id_book}] {book.title} - {book.author}")

            case "4": #Add a book
                id_book = input("Book id (integer): ").strip()
                title = input("Book title: ").strip()
                author = input("Book author: ").strip()

                if not id_book.isdigit():
                    print("ID must be an integer.")
                    continue
                id_book = int(id_book)

                book = Book(id_book=id_book, title=title, author=author, status=Status_book.available)
                library.add_book(book)
                print("Book added!")


            case "5": #Add a user
                id_user = input("User id (integer): ").strip()
                name = input("User name: ").strip()

                if not id_user.isdigit():
                    print("ID must be an integer.")
                    continue
                id_user = int(id_user)

                user = User(id_user=id_user, user_name=name, borrowed_books=[])
                library.create_user(user)
                print("User added!")

            case "6": #Remove a book
                id_book = input("Book id: ").strip()

                if not id_book.isdigit():
                    print("ID must be an integer.")
                    continue
                id_book = int(id_book)
                library.remove_book(id_book)
                print("Book removed!")

            case "7": #Remove a user
                id_user = input("User id: ").strip()

                if not id_user.isdigit():
                    print("ID must be an integer.")
                    continue
                id_user = int(id_user)
                library.remove_user(id_user)
                print("User removed!")

            case "8": #Search for a book
                print("How do you want to search?")
                print(" 1 - By title")
                print(" 2 - By author")
                print(" 3 - By keyword")

                search_choice = input("Your choice: ").strip()
                results = []

                match search_choice:

                    case "1":  # Search by title
                        txt = input("Enter title or part of it: ").strip()
                        results = library.search_books(title=txt)

                    case "2":  # Search by author
                        txt = input("Enter author name or part of it: ").strip()
                        results = library.search_books(author=txt)

                    case "3":  # Search by keyword
                        txt = input("Enter a keyword: ").strip()
                        results = library.search_books(keyword=txt)

                    case _:
                        print("Invalid choice.")
                        continue

                if not results:
                    print("No books found.")
                else:
                    for b in results:
                        status = "available" if b.is_available() else "borrowed"
                        print(f"[{b.id_book}] {b.title} - {b.author} ({status})")

            case "9": # Loan a book
                id_user = input("User id: ").strip()
                id_book = input("Book id: ").strip()

                if not id_user.isdigit() or not id_book.isdigit():
                    print("Both IDs must be integers.")
                    continue
                id_user = int(id_user)
                id_book = int(id_book)
                library.loan_book(id_user,id_book)
                print("Book borrowed!")

            case "10": #Return a book
                id_user = input("User id: ").strip()
                id_book = input("Book id: ").strip()

                if not id_user.isdigit() or not id_book.isdigit():
                    print("Both IDs must be integers.")
                    continue
                id_user = int(id_user)
                id_book = int(id_book)
                library.return_book(id_user, id_book)
                print("Book returned!")

            case "11": #Statistics
                stats = library.statistics()
                print(f"Number of books: {stats['Number of books']}")
                print(f"Number of users: {stats['Number of users']}")

            case "12": #The distribution plot
                library.plot_borrow_dist()

            case "0": #Quit
                print("Goodbye!")
                break

            case _:
                print("Invalid choice. Please enter a number between 0 and 12.")
                continue

if __name__ == "__main__":
    main()
