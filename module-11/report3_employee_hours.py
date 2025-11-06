import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="$opH2112",
    database="bacchus_winery"
)

cursor = db.cursor()

# Updated query using employeehours and department tables
cursor.execute("""
    SELECT department.department_name, employee.first_name, employee.last_name, 
           SUM(employeehours.hours_worked) AS total_hours
    FROM employeehours
    JOIN employee ON employeehours.employee_id = employee.employee_id
    JOIN department ON employee.department_id = department.department_id
    GROUP BY department.department_name, employee.employee_id
    ORDER BY total_hours DESC;
""")

results = cursor.fetchall()

print("Employee Hours by Department:")
for row in results:
    print(f"Department: {row[0]}, Employee: {row[1]} {row[2]}, Total Hours: {row[3]}")

db.close()
