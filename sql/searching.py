import mysql.connector

# Step 1: Connect to the 'testdb' database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Parshu@13",
    database="testdb"
)

cursor = conn.cursor()
# cursor.execute("SELECT * FROM employees WHERE age =30")
cursor.execute("SELECT * FROM employees WHERE name LIKE '%J%'")
result = cursor.fetchall()
for x in result:
    print(x)