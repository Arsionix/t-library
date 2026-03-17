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

    while True:
        clear_screen()
        show_menu()
        choice = input("Выберите действие (1-8): ")

        if choice == "1":
            print("\n--- Добавление книги ---")
            title = input("Название: ")
            author = input("Автор: ")
            genre = input("Жанр: ")

            book = Book(title, author, genre)
            library.add_book(book)

            input("\nНажмите Enter чтобы продолжить...")

        elif choice == "2":
            print("\n--- Просмотр книг ---")

            if not library.get_all_books():
                print("\nВ библиотеке пока нет книг.")
                input("\nНажмите Enter чтобы продолжить...")
                continue

            print("\nКак сортировать?")
            print("1. По названию")
            print("2. По автору")
            print("3. По жанру")
            print("4. Без сортировки")

            sort_choice = input("Выберите (1-4): ")

            if sort_choice == "1":
                books = library.get_sorted_books("title")
            elif sort_choice == "2":
                books = library.get_sorted_books("author")
            elif sort_choice == "3":
                books = library.get_sorted_books("genre")
            else:
                books = library.get_all_books()

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
                library.toggle_favorite(book_id)
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

        elif choice == "8":
            print("До свидания!")
            break
        else:
            print(f"\nФункция {choice} в разработке...")
            input("Нажмите Enter чтобы продолжить...")


if __name__ == "__main__":
    main()
