#     Developer: Timmy Bell
# Creation Date: 11/12/2022
#         Class: CSD 310
#    Assignment: Module 7.2

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

# Queries
cursor.execute("SELECT studio_id, studio_name FROM movies.studio")
studio = cursor.fetchall()
print('-- DISPLAYING Studio RECORDS --')
for studio_id, studio_name in studio:
    print("Studio ID: {} \n Studio Name: {}\n".format(studio_id, studio_name))

cursor.execute("SELECT genre_id, genre_name FROM movies.genre")
genre = cursor.fetchall()
print('-- DISPLAYING Genre RECORDS -- ')
for genre_id, genre_name in genre:
    print("Genre ID: {} \n Genre Name: {}\n".format(genre_id, genre_name))

cursor.execute("SELECT film_name, film_runtime FROM movies.film WHERE film_runtime < 120")
film = cursor.fetchall()
print('-- DISPLAYING Short Film RECORDS -- ')
for film_name, film_runtime in film:
    print("Film Name: {} \n Runtime: {}\n".format(film_name, film_runtime))

cursor.execute("SELECT film_name, film_director FROM movies.film Order By film_director")
film = cursor.fetchall()
print('-- DISPLAYING Director RECORDS in Order -- ')
for film_name, film_director in film:
    print("Film Name: {} \n Director: {}\n".format(film_name, film_director))
