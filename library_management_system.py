class Book:
    def __init__(self, title, author, isbn, total_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        else:
            return False

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        else:
            return False

class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) < 3 and book.borrow():
            self.borrowed_books.append(book)
            return True
        else:
            return False

    def return_book(self, book):
        if book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            return True
        else:
            return False

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def add_patron(self, patron):
        self.patrons.append(patron)

    def borrow_book(self, patron, book):
        if patron in self.patrons and book in self.books and book.available_copies > 0:
            if patron.borrow_book(book):
                return True
            else:
                return False
        else:
            return False

    def return_book(self, patron, book):
        if patron in self.patrons and book in self.books and book in patron.borrowed_books:
            if patron.return_book(book):
                return True
            else:
                return False
        else:
            return False

class Catalog:
    def __init__(self, library):
        self.library = library

    def display_all_books(self):
        print("All Books:")
        for book in self.library.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Available Copies: {book.available_copies}")

    def display_all_patrons(self):
        print("\nAll Patrons:")
        for patron in self.library.patrons:
            print(f"Name: {patron.name}, Patron ID: {patron.patron_id}, Borrowed Books: {len(patron.borrowed_books)}")

def display_menu():
    print("\nLibrary Management System Menu:")
    print("1. Display All Books")
    print("2. Display All Patrons")
    print("3. Borrow a Book")
    print("4. Return a Book")
    print("5. Exit")
    return input("Select an option: ")

def main():
    library = Library()
    book1 = Book("Book 1", "Author 1", "love", 2)
    book2 = Book("Book 2", "Author 2", "power", 3)
    patron1 = Patron("Patron 1", "P010")
    patron2 = Patron("Patron 2", "P078")

    library.add_book(book1)
    library.add_book(book2)
    library.add_patron(patron1)
    library.add_patron(patron2)

    catalog = Catalog(library)

    while True:
        choice = display_menu()

        if choice == "1":
            catalog.display_all_books()
        elif choice == "2":
            catalog.display_all_patrons()
        elif choice == "3":
            patron_id = input("Enter Patron ID: ")
            book_isbn = input("Enter Book ISBN: ")
            patron = next((p for p in library.patrons if p.patron_id == patron_id), None)
            book = next((b for b in library.books if b.isbn == book_isbn), None)
            if patron and book:
                if library.borrow_book(patron, book):
                    print("Book borrowed successfully.")
                else:
                    print("Borrowing failed.")
            else:
                print("Invalid patron or book information.")
        elif choice == "4":
            patron_id = input("Enter Patron ID: ")
            book_isbn = input("Enter Book ISBN: ")
            patron = next((p for p in library.patrons if p.patron_id == patron_id), None)
            book = next((b for b in library.books if b.isbn == book_isbn), None)
            if patron and book:
                if library.return_book(patron, book):
                    print("Book returned successfully.")
                else:
                    print("Returning failed.")
            else:
                print("Invalid patron or book information.")
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()