# Jackson Webster
# Module 8.2 Assignment - Movies Update and Delete
# This program connects to the movies database, displays films,
# then performs insert, update, and delete operations.

import mysql.connector
from mysql.connector import errorcode
from dotenv import dotenv_values

# Load credentials
secrets = dotenv_values("C:/csd/csd-310/module-8/config.env")

config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

# Connect to database
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
        print(f"Genre Name ID: {film[2]}")
        print(f"Studio Name: {film[3]}\n")


# Step 1: Display all current films
show_films(cursor, "DISPLAYING FILMS")

# Clean up any test data (so we don’t have duplicates)
cursor.execute("DELETE FROM film WHERE film_name = 'Inception'")
db.commit()

# Step 2: Insert a new film record (Inception)
cursor.execute("""
    INSERT INTO film (film_name, film_director, genre_id, studio_id, film_releaseDate, film_runtime)
    VALUES ('Inception', 'Christopher Nolan', 2, 1, '2010', 148)
""")
db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

# Step 3: Update the film 'Alien' to the Horror genre
cursor.execute("""
    UPDATE film
    SET genre_id = 1
    WHERE film_name = 'Alien'
""")
db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")

# Step 4: Delete the film 'Gladiator'
cursor.execute("""
    DELETE FROM film
    WHERE film_name = 'Gladiator'
""")
db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

# Step 5: Close connection
db.close()