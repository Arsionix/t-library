class Library:

    def __init__(self):
        self.books = []
        self.next_id = 1

    def add_book(self, book):
        book.id = self.next_id
        self.books.append(book)
        self.next_id += 1
        print(f"\nКнига '{book.title}' добавлена!")

    def get_all_books(self):
        return self.books
