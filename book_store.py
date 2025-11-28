class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
    def get_age(self):
        CURRENT_YEAR = 2025
        return CURRENT_YEAR - self.publication_year

    def get_summary(self):
        return f"Title: {self.title}, Author: {self.author}, Published: {self.publication_year}"
if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", "9780451524935", 1949)
    book2 = Book("The Hobbit", "J.R.R. Tolkien", "9780261103344", 1937)

    for b in (book1, book2):
        print("Title:", b.title)
        print("Author:", b.author)
        print("ISBN:", b.isbn)
        print("Age:", b.get_age(), "years")
        print("Summary:", b.get_summary())
        print("-" * 40)