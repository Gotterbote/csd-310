#     Developer: Timmy Bell
# Creation Date: 11/22/2022
#         Class: CSD 310
#    Assignment: Module 8.2

import  mysql.connector
from mysql.connector import errorcode

# Declare a blank database variable
db = ""

# Method to configure database connection
def connect():
    global db
    config = {
        'user': 'movies_user',
        'password': 'popcorn',
        'host': 'localhost',
        'port': '3307',
        'database': 'movies',
        'raise_on_warnings': True
    }

    try:
        db = mysql.connector.connect(**config)

        print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

        input("\n\n Press any key to continue...")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("  The supplied username or password is invalid")

        elif err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("  The specified database does not exist")

        else:
            print(err)

    return db

# Establish connection
connect()
cursor = db.cursor()

def show_films(cursor, title):
    # Method to execute an inner join on all tables,
    #   iterate over the dataset and output the results to the terminal window.


    # Inner join query
    cursor.execute("SELECT film_name as Name, film_director as Director, studio_name as 'Studio Name', genre_name as Genre FROM film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

    # Get the results from the cursor object
    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    # Iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nStudio Name: {}\nGenre Name: {}\n".format(film[0], film[1],film[2], film[3]))

show_films(cursor, "DISPLAYING FILMS")

cursor.execute("INSERT INTO Film (film_id, film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES (4, 'Jurrasic World', 2015, 124, 'Colin Trevorrow', 3, 2) ")

show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

cursor.execute("UPDATE film SET genre_id = 1 WHERE film_name = 'Alien'")

show_films(cursor, "DISPLAYING FILMS AFTER update- Changed Alien to Horror")

cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")

show_films(cursor, "DISPLAYING FILMS AFTER DELETE")
