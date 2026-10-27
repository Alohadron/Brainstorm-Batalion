movies = []
def add_movies(movies):
    name = input("Enter the name of the movie: ")
    if name in movies:
        print("Movie name already added")
    elif name == "":
        print("Movie title cannot be empty")
    else:
        movies.append(name)
        print("Movie added successfully")

def display_movies(movies):
    # index = int(movies)
    print(f"Movies: {movies}")

def find_movies(movies):
    name = input("Enter the movie name: ")
    if name in movies:
        print("Movie found")
    else:
        print("Movie not found")
import random
def recommend_movies(movies):
    if len(movies) == 0:
        print("The list is empty")
    else:
        movie = random.choice(movies)
        print(f"Recommended movie: {movie}")

def main():
    pass
while True:
    print("\n---MOVIE MENU---")
    print("1. Add movie")
    print("2. Display all movies")
    print("3. Find a movie")
    print("4. Recommend a movie")
    print("5. Exit")

    option = int(input("Choose an option:"))
    match option:
        case 1:
            add_movies(movies)
        case 2:
            display_movies(movies)
        case 3:
            find_movies(movies)
        case 4:
            recommend_movies(movies)
        case 5:
            print("Exit")
            break
        case _:
            print("Invalid choice")