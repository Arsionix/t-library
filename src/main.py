from book import Book
from library import Library
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu():
    print("\n" + "="*40)
    print(" "*14 + "Т-БИБЛИОТЕКА")
    print("="*40)
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Добавить в избранное")
    print("4. Изменить статус прочтения")
    print("5. Показать избранное")
    print("6. Удалить книгу")
    print("7. Поиск книг")
    print("8. Сохранить и выйти")
    print("="*40)


def main():
    library = Library()

    print("Загрузка библиотеки...")
    library.load_from_file()
    input("\nНажмите Enter чтобы продолжить...")

    while True:
        clear_screen()
        show_menu()
        choice = input("Выберите действие (1-8): ")

        if choice == "1":
            print("\n--- Добавление книги ---")
            title = input("Название: ")
            author = input("Автор: ")
            genre = input("Жанр: ")
            year = input("Год издания: ")
            description = input("Краткое описание: ")

            book = Book(title, author, genre, year, description)
            library.add_book(book)
            library.save_to_file()

            input("\nНажмите Enter чтобы продолжить...")

        elif choice == "2":
            print("\n--- Просмотр книг ---")

            if not library.get_all_books():
                print("\nВ библиотеке пока нет книг.")
                input("\nНажмите Enter чтобы продолжить...")
                continue

            print("\nФильтрация книг:")
            print("1. Показать все книги")
            print("2. Фильтр по жанру")
            print("3. Фильтр по статусу прочтения")
            print("4. Фильтр по жанру и статусу")

            filter_choice = input("Выберите тип фильтра (1-4): ")

            genre_filter = None
            status_filter = None

            if filter_choice == "2":
                genres = library.get_all_genres()
                if genres:
                    print("\nДоступные жанры:")
                    for i, genre in enumerate(genres, 1):
                        print(f"{i}. {genre}")

                    try:
                        genre_num = int(input("\nВыберите номер жанра: ")) - 1
                        if 0 <= genre_num < len(genres):
                            genre_filter = genres[genre_num]
                        else:
                            print("Неверный номер жанра!")
                    except ValueError:
                        print("Ошибка! Введите число.")
                else:
                    print("Нет доступных жанров для фильтрации!")

            elif filter_choice == "3":
                print("\nВыберите статус:")
                print("1. Прочитанные")
                print("2. Непрочитанные")

                status_choice = input("Выберите (1-2): ")
                if status_choice == "1":
                    status_filter = True
                elif status_choice == "2":
                    status_filter = False
                else:
                    print("Неверный выбор статуса!")

            elif filter_choice == "4":
                genres = library.get_all_genres()
                if genres:
                    print("\nДоступные жанры:")
                    for i, genre in enumerate(genres, 1):
                        print(f"{i}. {genre}")

                    try:
                        genre_num = int(input("\nВыберите номер жанра: ")) - 1
                        if 0 <= genre_num < len(genres):
                            genre_filter = genres[genre_num]

                            print("\nВыберите статус:")
                            print("1. Прочитанные")
                            print("2. Непрочитанные")

                            status_choice = input("Выберите (1-2): ")
                            if status_choice == "1":
                                status_filter = True
                            elif status_choice == "2":
                                status_filter = False
                            else:
                                print("Неверный выбор статуса!")
                        else:
                            print("Неверный номер жанра!")
                    except ValueError:
                        print("Ошибка! Введите число.")
                else:
                    print("Нет доступных жанров для фильтрации!")

            if filter_choice in ["2", "3", "4"]:
                books_to_sort = library.get_filtered_books(
                    genre_filter, status_filter)
                if not books_to_sort:
                    print("\nПо заданным фильтрам книг не найдено!")
                    input("\nНажмите Enter чтобы продолжить...")
                    continue
            else:
                books_to_sort = library.get_all_books()

            print("\nКак сортировать?")
            print("1. По названию")
            print("2. По автору")
            print("3. По жанру")
            print("4. По году издания")
            print("5. Без сортировки")

            sort_choice = input("Выберите (1-5): ")

            if sort_choice == "1":
                books = library.get_sorted_books("title")
                if filter_choice in ["2", "3", "4"]:
                    books = [b for b in books if b in books_to_sort]
            elif sort_choice == "2":
                books = library.get_sorted_books("author")
                if filter_choice in ["2", "3", "4"]:
                    books = [b for b in books if b in books_to_sort]
            elif sort_choice == "3":
                books = library.get_sorted_books("genre")
                if filter_choice in ["2", "3", "4"]:
                    books = [b for b in books if b in books_to_sort]
            elif sort_choice == "4":
                books = library.get_sorted_books("year")
                if filter_choice in ["2", "3", "4"]:
                    books = [b for b in books if b in books_to_sort]
            else:
                books = books_to_sort if filter_choice in [
                    "2", "3", "4"] else library.get_all_books()

            if filter_choice in ["2", "3", "4"]:
                print(f"\nОтфильтровано книг: {len(books)}")
            library.print_books(books)

            input("\nНажмите Enter чтобы продолжить...")

        elif choice == "3":
            print("\n--- Избранное ---")

            if not library.get_all_books():
                print("\nВ библиотеке пока нет книг.")
                input("\nНажмите Enter чтобы продолжить...")
                continue

            library.print_books(library.get_all_books())

            try:
                book_id = int(input("\nВведите ID книги: "))
                if library.toggle_favorite(book_id):
                    library.save_to_file()
            except ValueError:
                print("Ошибка! Введите число.")

            input("\nНажмите Enter чтобы продолжить...")

        elif choice == "4":
            print("\n--- Изменение статуса прочтения ---")

            if not library.get_all_books():
                print("\nВ библиотеке пока нет книг.")
                input("\nНажмите Enter чтобы продолжить...")
                continue

            library.print_books(library.get_all_books())

            try:
                book_id = int(input("\nВведите ID книги: "))
                if library.toggle_read(book_id):
                    library.save_to_file()
            except ValueError:
                print("Ошибка! Введите число.")

            input("\nНажмите Enter чтобы продолжить...")

        elif choice == "5":
            print("\n--- Избранные книги ---")

            favorites = library.get_favorite_books()
            if favorites:
                library.print_books(favorites)
            else:
                print("\nВ избранном пока нет книг.")

            input("\nНажмите Enter чтобы продолжить...")

        elif choice == "6":
            print("\n--- Удаление книги ---")

            if not library.get_all_books():
                print("\nВ библиотеке пока нет книг.")
                input("\nНажмите Enter чтобы продолжить...")
                continue

            library.print_books(library.get_all_books())

            try:
                book_id = int(input("\nВведите ID книги для удаления: "))
                book = library.find_book_by_id(book_id)
                if book:
                    print(f"\nВы точно хотите удалить '{book.title}'?")
                    confirm = input("Да/Нет (д/н): ")
                    if confirm.lower() in ['да', 'д', 'yes', 'y']:
                        if library.delete_book(book_id):
                            library.save_to_file()
                    else:
                        print("Удаление отменено.")
            except ValueError:
                print("Ошибка! Введите число.")

            input("\nНажмите Enter чтобы продолжить...")

        elif choice == "7":
            print("\n--- Поиск книг ---")

            if not library.get_all_books():
                print("\nВ библиотеке пока нет книг.")
                input("\nНажмите Enter чтобы продолжить...")
                continue

            keyword = input("Введите слово для поиска: ")

            if keyword.strip():
                results = library.search_books(keyword)

                if results:
                    print(f"\nНайдено книг: {len(results)}")
                    library.print_books(results)
                else:
                    print(f"\nКниги по запросу '{keyword}' не найдены.")
            else:
                print("Вы ничего не ввели!")

            input("\nНажмите Enter чтобы продолжить...")

        elif choice == "8":
            print("\nСохраняем библиотеку...")
            library.save_to_file()
            print("До свидания!")
            break
        else:
            print(f"\nНеверный выбор! Введите число от 1 до 8.")
            input("Нажмите Enter чтобы продолжить...")


if __name__ == "__main__":
    main()
