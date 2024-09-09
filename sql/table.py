import mysql.connector

# Step 1: Connect to the 'testdb' database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Parshu@13",
    database="testdb"
)

cursor = conn.cursor()

# Step 2: SQL query to create the 'departments' table
create_departments_table_query = """
CREATE TABLE IF NOT EXISTS departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
)
"""

# Step 3: Execute the query to create the 'departments' table
cursor.execute(create_departments_table_query)

# Step 4: Modify the 'employees' table to add a foreign key to 'departments'
alter_employees_table_query = """
ALTER TABLE employees
ADD COLUMN department_id INT,
ADD CONSTRAINT fk_department
FOREIGN KEY (department_id)
REFERENCES departments(department_id)
"""
cursor.execute(alter_employees_table_query)

# Step 5: Insert some test data into both tables
# Insert data into 'departments'
insert_departments_query = """
INSERT INTO departments (department_name) 
VALUES ('HR'), ('Engineering'), ('Sales')
"""
cursor.execute(insert_departments_query)

# Insert data into 'employees' (referencing 'departments')
insert_employees_query = """
INSERT INTO employees (name, age, department_id, joining_date)
VALUES
('John Doe', 30, 1, '2022-01-15'),
('Jane Smith', 28, 2, '2021-06-10'),
('Emily Davis', 35, 3, '2020-03-25')
"""
cursor.execute(insert_employees_query)

# Step 6: Commit the changes to the database
conn.commit()

print("Tables and data inserted successfully.")

# Step 7: Perform a JOIN query to retrieve data from both tables
join_query = """
SELECT employees.name, employees.age, departments.department_name
FROM employees
JOIN departments ON employees.department_id = departments.department_id
"""

# Execute the JOIN query
cursor.execute(join_query)

# Fetch and print the results
result = cursor.fetchall()
for row in result:
    print(row)

# Step 8: Close the cursor and the connection
cursor.close()
conn.close()
