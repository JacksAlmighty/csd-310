import mysql.connector

config = {
    "user": "root",
    "password": "$opH2112",  
    "host": "localhost",
    "database": "bacchus_winery"
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    tables = [
        "Department",
        "Employee",
        "EmployeeHours",
        "Supplier",
        "SupplyItem",
        "SupplyOrder",
        "Wine",
        "Distributor",
        "DistributionOrder"
    ]

    for table in tables:
        print(f"\n--- {table} ---")
        cursor.execute(f"SELECT * FROM {table}")
        results = cursor.fetchall()
        for row in results:
            print(row)

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'db' in locals() and db.is_connected():
        db.close()