# A movie collecion app without database

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []

# Showing the list of movies
def list():
    for movie in movies:       
        print(movie)
    
# Adding movies in the list
def add():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    movies.append({
        'title': title,
        'director': director,
        'year': year
    })
    return movies

# Finding the move by title
def find():
    search = input("Search by title of the movie:")
    for movie in movies:
        if movie['title'] == search:
            print(movie) 
            break
    else:
        print(f"No movie found with title {search}")    
            
user_options = {
    "a" : add,
    "l" : list,
    "f" : find  
}


def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selection_option = user_options[selection]
            selection_option()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)

menu()