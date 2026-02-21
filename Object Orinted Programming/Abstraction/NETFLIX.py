# Netflix_System.py
# Data Abstraction Example
# User cannot see internal movie database


class Netflix:

    def __init__(self):

        # Private data (Hidden)
        self.__movies = {
            "Action": ["Fast and Furious", "John Wick", "Mission Impossible"],
            "Comedy": ["Mr Bean", "Home Alone", "Mask"],
            "Horror": ["Conjuring", "Nun", "Insidious"],
            "SciFi": ["Interstellar", "Avatar", "Inception"]
        }

        self.__watchlist = []


    # Show categories
    def show_categories(self):

        print("\nAvailable Categories:")

        for c in self.__movies:
            print("-", c)


    # Show movies inside category
    def show_movies(self, category):

        if category in self.__movies:

            print("\nMovies in", category)

            for m in self.__movies[category]:
                print("-", m)

        else:
            print("Category Not Found")


    # Add movie to watchlist
    def add_watchlist(self, movie):

        self.__watchlist.append(movie)
        print("Movie Added to Watchlist")


    # Show watchlist
    def show_watchlist(self):

        print("\nYour Watchlist")

        for m in self.__watchlist:
            print("-", m)


    # Play movie
    def play_movie(self, movie):

        print("\nPlaying:", movie)
        print("Enjoy Your Movie!")



# Main Program

n = Netflix()

while True:

    print("\n===== NETFLIX MENU =====")
    print("1 Show Categories")
    print("2 Show Movies")
    print("3 Add Watchlist")
    print("4 Show Watchlist")
    print("5 Play Movie")
    print("6 Exit")

    ch = input("Enter Choice: ")

    if ch == '1':

        n.show_categories()

    elif ch == '2':

        cat = input("Enter Category: ")
        n.show_movies(cat)

    elif ch == '3':

        mv = input("Enter Movie Name: ")
        n.add_watchlist(mv)

    elif ch == '4':

        n.show_watchlist()

    elif ch == '5':

        mv = input("Enter Movie Name: ")
        n.play_movie(mv)

    elif ch == '6':

        print("Good Bye")
        break

    else:

        print("Wrong Choice")
        
        # i use the help of AI in making this but i learn fro this