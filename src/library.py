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
        elif sort_by == "year":
            return sorted(self.books, key=lambda book: book.year if book.year else 0)
        else:
            return self.books

    def get_filtered_books(self, genre=None, read_status=None):
        filtered = self.books.copy()

        if genre and genre != "все":
            filtered = [book for book in filtered if book.genre.lower()
                        == genre.lower()]

        if read_status is not None:
            filtered = [
                book for book in filtered if book.is_read == read_status]

        return filtered

    def get_all_genres(self):
        genres = set()
        for book in self.books:
            genres.add(book.genre)
        return sorted(list(genres))

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
            print(f"Год: {book.year}")
            print(f"Описание: {book.description}")
            print(f"Статус: {read_status} {fav_status}")
            print("-"*30)

    def delete_book(self, book_id):
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            print(f"\nКнига '{book.title}' удалена из библиотеки!")
            self._recalculate_next_id()
            return True
        else:
            print(f"\nКнига с ID {book_id} не найдена!")
            return False

    def search_books(self, keyword):
        keyword = keyword.lower()
        results = []

        for book in self.books:
            if keyword in book.title.lower():
                results.append(book)
            elif keyword in book.author.lower():
                results.append(book)
            elif keyword in book.genre.lower():
                results.append(book)
            elif keyword in book.description.lower():
                results.append(book)

        return results

    def save_to_file(self, filename='data/library.json'):
        import json
        import os

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        books_data = []
        for book in self.books:
            books_data.append({
                'id': book.id,
                'title': book.title,
                'author': book.author,
                'genre': book.genre,
                'year': book.year,
                'description': book.description,
                'is_read': book.is_read,
                'is_favorite': book.is_favorite
            })

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({
                'books': books_data,
                'next_id': self.next_id
            }, f, ensure_ascii=False, indent=2)

        print(f"\nДанные сохранены в файл {filename}")

    def load_from_file(self, filename='data/library.json'):
        import json

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

                self.books = []

                for book_data in data['books']:
                    from book import Book
                    book = Book(
                        title=book_data['title'],
                        author=book_data['author'],
                        genre=book_data['genre'],
                        year=book_data['year'],
                        description=book_data['description']
                    )
                    book.id = book_data['id']
                    book.is_read = book_data['is_read']
                    book.is_favorite = book_data['is_favorite']
                    self.books.append(book)

                if 'next_id' in data:
                    self.next_id = data['next_id']
                else:
                    self._recalculate_next_id()

                print(f"Загружено {len(self.books)} книг из файла")
                return True

        except FileNotFoundError:
            print("Файл с данными не найден. Создаём новую библиотеку.")
            self.next_id = 1
            return False
        except json.JSONDecodeError:
            print("Файл с данными повреждён. Начинаем с чистой библиотеки.")
            self.next_id = 1
            return False

    def _recalculate_next_id(self):
        if not self.books:
            self.next_id = 1
        else:
            max_id = max(book.id for book in self.books)
            self.next_id = max_id + 1
