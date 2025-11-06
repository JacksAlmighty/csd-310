import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="$opH2112",
    database="bacchus_winery"
)

cursor = db.cursor()

# Query: Top selling wines
cursor.execute("""
    SELECT wine.wine_name, SUM(distributionorder.quantity) AS total_sold
    FROM wine
    JOIN distributionorder ON wine.wine_id = distributionorder.wine_id
    GROUP BY wine.wine_name
    ORDER BY total_sold DESC;
""")

results = cursor.fetchall()

print("Top Selling Wines:")
print("-----------------")
for wine_name, total_sold in results:
    print(f"{wine_name}: {total_sold}")

db.close()
