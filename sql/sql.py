import mysql.connector

# Establishing the connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Parshu@13",
)
#  Mandate code is above
# if conn.is_connected():
#     print("Connection Established.")

# var1 = conn.cursor()
# var1.execute("CREATE TABLE customers  ")
# for x in var1:
#     print(x)