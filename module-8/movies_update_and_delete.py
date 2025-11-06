# Jackson Webster 
# Module 8.2 Assignment 
# 10/29/2025
# This program connects to the movies database, displays films,
# then performs insert, update, and delete operations.

import mysql.connector
from mysql.connector import errorcode
from dotenv import dotenv_values


secrets = dotenv_values("C:/csd/csd-310/module-8/config.env")

config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    def show_films(cursor, title):
        """Display film information with joins to genre and studio tables."""
        query = """
            SELECT film_name AS Name,
                   film_director AS Director,
                   genre_name AS Genre,
                   studio_name AS Studio
            FROM film
            INNER JOIN genre ON film.genre_id = genre.genre_id
            INNER JOIN studio ON film.studio_id = studio.studio_id
            ORDER BY film_name
        """
        cursor.execute(query)
        films = cursor.fetchall()

        print("\n-- {} --".format(title))
        for film in films:
            print(f"Film Name: {film[0]}")
            print(f"Director: {film[1]}")
            print(f"Genre Name: {film[2]}")
            print(f"Studio Name: {film[3]}\n")

    
    cursor.execute("DELETE FROM film WHERE film_name = 'Inception'")
    cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")
    db.commit()

    
    cursor.execute("""
        UPDATE film
        SET genre_id = 2
        WHERE film_name = 'Alien'
    """)
    db.commit()

    
    show_films(cursor, "DISPLAYING FILMS")

    
    cursor.execute("""
        INSERT INTO film (film_name, film_director, genre_id, studio_id, film_releaseDate, film_runtime)
        VALUES ('Gladiator', 'Ridley Scott', 3, 1, '2000', 155)
    """)
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    
    cursor.execute("""
        UPDATE film
        SET genre_id = 1
        WHERE film_name = 'Alien'
    """)
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")

    
    cursor.execute("""
        DELETE FROM film
        WHERE film_name = 'Gladiator'
    """)
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    else:
        print(err)
finally:
    db.close()