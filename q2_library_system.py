# Add a book to the catalog
def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)

# Borrow a book
def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)

# Return a book
def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)

# Register a member
def register_member(members, member_id):
    members.add(member_id)

# Show available books
def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")
    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            print(book_id, "-", details)


def main():
    catalog = {}
    borrowed_books = []
    members = set()

    # Add books
    add_book(catalog, 1, "Python ", "Anjali", 2020)
    add_book(catalog, 2, "Data Science", "supriya", 2021)
    add_book(catalog, 3, "AI ", "Yash", 2022)
    add_book(catalog, 4, "M L", "Deepak", 2023)

    # Register members
    register_member(members, 101)
    register_member(members, 102)
    register_member(members, 101)  # duplicate
    register_member(members, 103)

    # Borrow books
    borrow_book(catalog, borrowed_books, 1)
    borrow_book(catalog, borrowed_books, 2)

    # Return a book
    return_book(borrowed_books, 1)

    # Show available books
    show_available(catalog, borrowed_books)


main()
