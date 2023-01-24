import mysql.connector

# Connect to the database
con = mysql.connector.connect(user='root', password='newpassword', host='localhost', database='mydb')

# Create a cursor object
cursor = con.cursor()

# Define the query
query = "SELECT Department.NAME as 'Department Name', COUNT(Employee.ID) as 'Employee Count' FROM Department LEFT JOIN Employee ON Department.ID = Employee.DEPT_ID GROUP BY Department.NAME ORDER BY COUNT(Employee.ID) DESC, Department.NAME ASC;"

# Execute the query
cursor.execute(query)

# Fetch all results
results = cursor.fetchall()

# Print the desired result
for result in results:
    print(result)

# Close the cursor and the connection
cursor.close()
con.close()