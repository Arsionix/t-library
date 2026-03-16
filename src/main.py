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

        elif choice == "8":
            print("До свидания!")
            break
        else:
            print(f"\nФункция {choice} в разработке...")
            input("Нажмите Enter чтобы продолжить...")


if __name__ == "__main__":
    main()
