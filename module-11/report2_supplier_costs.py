import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="$opH2112",  
    database="bacchus_winery"
)

cursor = db.cursor()

cursor.execute("""
    SELECT supplyitem.item_name, SUM(supplyorder.quantity_ordered) AS total_ordered
    FROM supplyorder
    JOIN supplyitem ON supplyorder.item_id = supplyitem.item_id
    GROUP BY supplyitem.item_name
    ORDER BY total_ordered DESC;
""")

results = cursor.fetchall()

print("Supplier Items by Total Quantity Ordered:")
for row in results:
    print(f"{row[0]}: {row[1]} units")

cursor.close()
db.close()
