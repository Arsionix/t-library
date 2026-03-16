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

    def get_sorted_books(self, sort_by):
        if sort_by == "title":
            return sorted(self.books, key=lambda book: book.title.lower())
        elif sort_by == "author":
            return sorted(self.books, key=lambda book: book.author.lower())
        elif sort_by == "genre":
            return sorted(self.books, key=lambda book: book.genre.lower())
        else:
            return self.books

    def print_books(self, books_to_print):
        if not books_to_print:
            print("\nВ библиотеке пока нет книг.")
            return

        print("\n" + "-"*50)
        print(f"Всего книг: {len(books_to_print)}")
        print("-"*50)

        for book in books_to_print:
            read_status = "Прочитана" if book.is_read else "Не прочитана"
            fav_status = "В избранном" if book.is_favorite else ""

            print(f"ID: {book.id}")
            print(f"Название: {book.title}")
            print(f"Автор: {book.author}")
            print(f"Жанр: {book.genre}")
            print(f"Статус: {read_status} {fav_status}")
            print("-"*30)
