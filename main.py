genders = ["fiction", "nonfiction", "science", "biography", "children"]
books = {}

def add_book():
    print("Add one book")
    title = input("add title of book: ").strip()
    if title in books:
        print("the book already exists")
        return
    author = input("author of book: ").strip()
    gender = input(f"gender ({', '.join(genders)}): ").lower()
    if gender not in genders:
        print("gender invalid")
        return
    try: 
        copies = int(input("Copies of book: "))
        if copies < 1:
            raise ValueError
    except ValueError:
        print("Copies invalid")
        return
    books[title] = {
        "author": author,
        "gender": gender,
        "copies": copies,
        "copies_available": copies
    }
    print(f"book '{title}' added correctly")


def search_book():
    title_search = input("Name of the title: ").strip()
    book = books.get(title_search)
    if not book:
        print("Book not found")
        return
    print(f"Title: {title_search}\nAuthor: {book['author']}\nGender: {book['gender']}\nCopies: {book['copies']}\nCopies available: {book['copies_available']}")

def register_loan_book():
    title_search = input("Name of the title: ").strip()
    book = books.get(title_search)
    if not book:
        print("Book not found")
        return
    if book['copies_available'] == 0:
        print("No copies available for loan")
        return
    book['copies_available'] -= 1
    print("Loan registered")

def register_return_book():
    title_search = input("Name of the title: ").strip()
    book = books.get(title_search)
    if not book:
        print("Book not found")
        return
    if book['copies_available'] < book['copies']:
        book['copies_available'] += 1
        print("Copy returned correctly")
    else:
        print("There are no borrowed copies to return")

def deleted_book():
    title_search = input("Name of the title to delete: ").strip()
    book = books.get(title_search)
    if not book:
        print("Book not found")
        return
    if book['copies'] != book['copies_available']:
        print("You can't delete the book — there are borrowed copies")
        return
    del books[title_search]
    print("Book deleted")

def search_genders_book(): 
    gender = input(f"gender ({', '.join(genders)}): ").lower()
    if gender not in genders:
        print("gender invalid")
        return
    found = [title for title, book in books.items() if book['gender'] == gender]
    if found: 
        print("Books found:")
        for title in found:
            print(f"- {title}")
    else:
        print("No books found")

def inventory_summary():
    total_books = len(books)
    total_copies = sum(book['copies_available'] for book in books.values())
    print(f"Total books: {total_books}")
    print(f"Total copies available: {total_copies}")

def menu():
    opcion = {
        "1": add_book,
        "2": search_book,
        "3": register_loan_book,
        "4": register_return_book,
        "5": deleted_book,
        "6": search_genders_book,
        "7": inventory_summary,
        "8": exit
    }

    while True:
        print("\nLibrary management")
        print("1. Add book")
        print("2. Search book")
        print("3. Register loan")
        print("4. Register return")
        print("5. Delete book")
        print("6. List by genre")
        print("7. Show summary")
        print("8. Exit")

        action = input("Choose an option: ").strip()
        if action in opcion:
            opcion[action]()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()
