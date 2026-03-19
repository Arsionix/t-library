class Library:

    def __init__(self):
        self.books = []
        self.next_id = 1

    def add_book(self, book):
        book.id = self.next_id
        self.books.append(book)
        self.next_id += 1
        print(f"\nКнига '{book.title}' добавлена!")

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def toggle_favorite(self, book_id):
        book = self.find_book_by_id(book_id)
        if book:
            book.is_favorite = not book.is_favorite
            if book.is_favorite:
                print(f"\nКнига '{book.title}' добавлена в избранное!")
            else:
                print(f"\nКнига '{book.title}' убрана из избранного!")
            return True
        else:
            print(f"\nКнига с ID {book_id} не найдена!")
            return False

    def toggle_read(self, book_id):
        book = self.find_book_by_id(book_id)
        if book:
            book.is_read = not book.is_read
            if book.is_read:
                print(f"\nКнига '{book.title}' отмечена как прочитанная!")
            else:
                print(f"\nКнига '{book.title}' отмечена как непрочитанная!")
            return True
        else:
            print(f"\nКнига с ID {book_id} не найдена!")
            return False

    def get_favorite_books(self):
        favorites = [book for book in self.books if book.is_favorite]
        return favorites

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

    def delete_book(self, book_id):
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            print(f"\nКнига '{book.title}' удалена из библиотеки!")
            return True
        else:
            print(f"\nКнига с ID {book_id} не найдена!")
            return False
