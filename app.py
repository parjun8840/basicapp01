import datetime
import db
menu='''Please select one of the following options:
1) Add new movie
2) View upcoming movie
3) View all movies
4) Watch a movie
5) View watched movies
6) Exit

Your selection: '''
welcome="Welcome to the Movie App"

def prompt_add_movie():
    title = input ("Add Title: ")
    release_date = input("Release date (dd-mm-YYYY)")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()
    db.add_movie(title, timestamp)

def print_movie_list(heading, movies):
    print(f"## {heading} movies ##")
    i = 1
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[1]) 
        human_date = movie_date.strftime("%b %d %Y")
        print(f"{i}) {movie[0]} (on {human_date})")
        i = i+1
    print("###########################\n")


def prompt_watch_movie():
    movie_title = input("Enter movie title you've watched: ")
    db.watch_movie(movie_title)


print(welcome)
db.create_table()

while (user_input := input(menu)) != "6":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = db.get_movies(True)
        print_movie_list("Upcoming", movies)
    elif user_input == "3":
        movies = db.get_movies()
        if len(movies) == 0:
            print("\nYou don't have any movie added to the list\n")
        else:
            print_movie_list("All", movies)
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
        movies = db.get_watched_movies()
        print_movie_list("Watched", movies)
    else:
        print("Invalid input, please try again!")