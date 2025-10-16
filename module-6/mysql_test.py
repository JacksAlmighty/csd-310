import mysql.connector
from mysql.connector import errorcode
import dotenv
from dotenv import dotenv_values

secrets = dotenv_values("C:/csd/csd-310/module-6/config.env")

config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print(f"Database user {config['user']} connected to MySQL on host {config['host']} with database {config['database']}")
    input("\nPress any key to continue...")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
finally:
    db.close()