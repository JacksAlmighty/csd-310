import mysql.connector

# Connect to the Bacchus Winery
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="$opH2112",   
    database="bacchus_winery"
)

cursor = db.cursor()

query = """
SELECT 
    d.distributor_name AS Distributor,
    SUM(o.quantity) AS Total_Quantity_Sold
FROM Distributor d
JOIN DistributionOrder o
    ON d.distributor_id = o.distributor_id
GROUP BY d.distributor_name
ORDER BY Total_Quantity_Sold DESC;
"""

cursor.execute(query)
results = cursor.fetchall()

print("Distributor Sales Summary")
print("-------------------------")

for row in results:
    distributor = row[0]
    total_sold = row[1]
    print(f"{distributor}: {total_sold}")

cursor.close()
db.close()
