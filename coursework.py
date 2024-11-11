class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        return f"{self.title} by {self.author}, published in {self.year_published}"


def sort_books_by_year(books):
    """Sorts a list of Book objects by year published.

    Args:
        books: A list of tuples, where each tuple contains (title, author, year).

    Returns:
        A sorted list of Book objects.
    """

    if not books:
        return []

    return sorted(books, key=lambda book: book.year_published)

book1 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1954)
book2 = Book("Pride and Prejudice", "Jane Austen", 1813)
book3 = Book("Oliver Twist", "Charles Dickens",1863)
book4 = Book("Frankenstein", "Mary Shelley",1818)
book5 = Book("Beloved", "Toni Morrison",1987)


print(book1.describe())
print(book2.describe())
print(book3.describe())
print(book4.describe())
print(book5.describe())


books = [book1, book2, book3, book4, book5]
sorted_books = sort_books_by_year(books)
print("\nFor loop:")
for book in sorted_books:
    print(f"Title: {book.title}, Author: {book.author}, Year: {book.year_published}")


print("\nWhile loop:")
i = 0
while i < len(sorted_books):
    book = sorted_books[i]
    print(f"Title: {book.title}, Author: {book.author}, Year: {book.year_published}")
    i += 1


while True:
    title_to_search = input("Enter a book title to search (or 'exit' to quit): ")
    if title_to_search.lower() == "exit":
        break

    found = False
    for book in sorted_books:
        if book.title.lower() == title_to_search.lower():
            print(f"Found: {book.describe()}")
            found = True
            break

    if not found:
        print("Book not found.")