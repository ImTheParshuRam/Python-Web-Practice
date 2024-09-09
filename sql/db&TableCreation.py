import mysql.connector

# Step 1: Establish connection to MySQL server (without specifying a database)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Parshu@13",
)

cursor = conn.cursor()

# Step 2: SQL query to create a new database
create_database_query = "CREATE DATABASE IF NOT EXISTS testdb"
cursor.execute(create_database_query)

print("Database created successfully.")

# Step 3: Close the initial connection (optional but good practice)
cursor.close()
conn.close()

# Step 4: Re-establish connection, this time to the newly created 'testdb' database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Parshu@13",
    database="testdb"
)

cursor = conn.cursor()

# Step 5: SQL query to create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    department VARCHAR(50),
    joining_date DATE
)
"""

# Step 6: Execute the query to create the table
cursor.execute(create_table_query)

# Step 7: Commit the changes
conn.commit()

# Step 8: Close the cursor and connection
cursor.close()
conn.close()

print("Table created successfully.")


