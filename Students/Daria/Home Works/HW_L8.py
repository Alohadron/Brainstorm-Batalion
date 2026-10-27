import random
def add_movie(movies):
    name = input('Enter ovie title:')
    if name == "":
        print("Movie title cannot be empty!")
    elif name in movies:
        print("This movie alredy in the collection!")
    else: 
        movies.append(name)
        print("Movie added successefully!")

def display_movies(movies):
    if len(movies) == 0:
        print("The collection is empty.")
    else:
        print("Movie collection:")
        for i in range(len(movies)):
            print(i + 1, ".", movies[i])

def find_movie(movies):
    name = input("Enter movie title to find: ")

    if name in movies:
        print("Movie found!")
    else:
        print("Movie not found. ")

def recommendet_movie(movies):
    if len(movies) == 0:
        print("The collection is empty.")
    else: 
        movie = random.choice(movies)
        print("Recommendet movie:", movie)

def count_movies(movies): 
    print("Nuber of movies:", len(movies))

def main():
    movies = []

    while True:
        print("\n==== MOVIE COLLECTION ====")
        print("1. Add movie")
        print("2. Display all movies")
        print("3. Find a movie")
        print("4. Recommendet movie")
        print("5. Count movies")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_movie(movies)
        elif choice == "2":
            display_movies(movies)
        elif choice == "3":
            find_movie(movies)
        elif choice =="4":
            recommendet_movie(movies)
        elif choice == "5":
            count_movies(movies)
        elif choice == "6":
            print("Goodbye!")
            break
        else: print("Invalid option. Try again!")
main()
