class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def description(self):
        return f"{self.title} by {self.author}, published in {self.year_published}"
# 
book1 = Book("Great Expectations", "Charles Dickens", 1861)
book2 = Book("Romeo and Juliet", "William Shakespeare", 1597)
book3 = Book("Oliver Twist", "Charles Dickens",1863)
book4 = Book("Frankenstein", "Mary Shelley",1818)
book5 = Book("Beloved", "Toni Morrison",1987)
print(book1.description())
print(book2.description())
print(book3.description())
print(book4.description())
print(book5.description())

def sort_books_by_year(books):
    if not books:
        return "The book list is empty."
    return sorted(books, key=lambda book: book.year_published)

sorted_books = sort_books_by_year([book1, book2])

for book in sorted_books:
    print(book.description())

index = 0
while index < len(sorted_books):
    print(sorted_books[index].description())
    index += 1  

    def search_books_by_title(books):
        while True:
        search_books_by_title= input("Enter the book title to search (or type 'exit' to stop): ")
        if title.lower() == "exit":
            print("Exiting the search.")
            break
        found_books = [book for book in books if book.title.lower() == title.lower()]
        if found_books:
            for book in found_books:
                print(book.description())
        else:
            print("Book not found.")

