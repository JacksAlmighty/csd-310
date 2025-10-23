#Jackson Webster
#10/23/2025
#Module 7.2 Assignment
#This program connects to a MySQL database and displays lists of studios, genres, short films, and films grouped by director in a clear, organized format.

import mysql.connector
from mysql.connector import errorcode
from dotenv import dotenv_values


secrets = dotenv_values("C:/csd/csd-310/module-7/config.env")

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

    
    cursor.execute("SELECT * FROM studio")
    studios = cursor.fetchall()
    print("-- DISPLAYING Studio RECORDS --")
    for studio in studios:
        print(f"Studio ID: {studio[0]}")
        print(f"Studio Name: {studio[1]}\n")

    
    cursor.execute("SELECT * FROM genre")
    genres = cursor.fetchall()
    print("-- DISPLAYING Genre RECORDS --")
    for genre in genres:
        print(f"Genre ID: {genre[0]}")
        print(f"Genre Name: {genre[1]}\n")

    
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    short_films = cursor.fetchall()
    print("-- DISPLAYING Short Film RECORDS --")
    for film in short_films:
        print(f"Film Name: {film[0]}")
        print(f"Runtime: {film[1]}\n")

    
    cursor.execute("SELECT film_director, film_name FROM film ORDER BY film_director, film_name")
    films_by_director = cursor.fetchall()
    print("-- DISPLAYING Director RECORDS in Order --")
    current_director = ""
    for film in films_by_director:
        if film[0] != current_director:
            current_director = film[0]
            print(f"\nDirector: {current_director}")
        print(f"Film Name: {film[1]}")

finally:
    db.close()