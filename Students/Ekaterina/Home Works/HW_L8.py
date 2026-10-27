import random


def add_movie(movies):
    title = input("Введите название фильма: ").strip()

    if not title:
        print("Ошибка: Название фильма не может быть пустым!")
        return

    if any(movie.lower() == title.lower() for movie in movies):
        print(f"Фильм '{title}' уже есть в коллекции!")
    else:
        movies.append(title)
        print(f"Фильм '{title}' успешно добавлен в коллекцию!")


def display_movies(movies):
    if not movies:
        print(" Ваша коллекция фильмов пуста.")
        return

    print("\n--- Список фильмов ---")
    for index, movie in enumerate(movies, 1):
        print(f"{index}. {movie}")
    print("-" * 22)


def count_movies(movies):
    count = len(movies)
    print(f"Всего фильмов в коллекции: {count}")


def find_movie(movies):
    if not movies:
        print("📭 Коллекция пуста, искать нечего.")
        return

    title = input("Введите название фильма для поиска: ").strip()
    if not title:
        print("Ошибка: Название не может быть пустым.")
        return

    found = [movie for movie in movies if movie.lower() == title.lower()]

    if found:
        print(f"Фильм '{found[0]}' найден в вашей коллекции!")
    else:
        print(f"Фильм '{title}' не найден в коллекции.")


def recommend_movie(movies):
    if not movies:
        print("📭 Коллекция пуста. Невозможно предложить рекомендацию.")
        return

    recommended = random.choice(movies)
    print(f"🎬 Рекомендуем посмотреть: '{recommended}'! Приятного просмотра! 🍿")


def main():
    movies = []

    while True:
        print("\n===== MOVIE COLLECTION =====")
        print("1. Add movie")
        print("2. Display all movies")
        print("3. Find a movie")
        print("4. Recommend a movie")
        print("5. Count movies")
        print("6. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            add_movie(movies)
        elif choice == "2":
            display_movies(movies)
        elif choice == "3":
            find_movie(movies)
        elif choice == "4":
            recommend_movie(movies)
        elif choice == "5":
            count_movies(movies)
        elif choice == "6":
            print("Программа завершена. До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 6.")


if __name__ == "__main__":
    main()