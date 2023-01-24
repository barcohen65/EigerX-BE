import mysql.connector

"CREATE DATABASE mydb;"
# Connect to the database
con = mysql.connector.connect(user='root', password='newpassword', host='localhost')

# Create a cursor object
cursor = con.cursor()

# Create the database
cursor.execute("CREATE DATABASE departmentsum;")
cursor.execute("USE departmentsum;")

# Create the Department table
cursor.execute("CREATE TABLE Department (ID INT PRIMARY KEY, NAME VARCHAR(255), LOCATION VARCHAR(255));")
cursor.execute("INSERT INTO DEPARTMENT (ID, NAME, LOCATION) VALUES (1, 'Executive', 'Sydney');")
cursor.execute("INSERT INTO DEPARTMENT (ID, NAME, LOCATION) VALUES (2, 'Production', 'Sydney');")
cursor.execute("INSERT INTO DEPARTMENT (ID, NAME, LOCATION) VALUES (3, 'Resources', 'Cape Town');")
cursor.execute("INSERT INTO DEPARTMENT (ID, NAME, LOCATION) VALUES (4, 'Technical', 'Texas');")
cursor.execute("INSERT INTO DEPARTMENT (ID, NAME, LOCATION) VALUES (5, 'Management', 'Paris');")

# Create the Employee table
cursor.execute("CREATE TABLE Employee (ID INT PRIMARY KEY, NAME VARCHAR(255), SALARY INT, DEPT_ID INT, FOREIGN KEY(DEPT_ID) REFERENCES Department(ID));")
cursor.execute("INSERT INTO EMPLOYEE (ID, NAME, SALARY, DEPT_ID) VALUES (1, 'Candice', 4685, 1);")
cursor.execute("INSERT INTO EMPLOYEE (ID, NAME, SALARY, DEPT_ID) VALUES (2, 'Julia', 2559, 2);")
cursor.execute("INSERT INTO EMPLOYEE (ID, NAME, SALARY, DEPT_ID) VALUES (3, 'Bob', 4405, 4);")
cursor.execute("INSERT INTO EMPLOYEE (ID, NAME, SALARY, DEPT_ID) VALUES (4, 'Scarlet', 4685, 1);")
cursor.execute("INSERT INTO EMPLOYEE (ID, NAME, SALARY, DEPT_ID) VALUES (5, 'Ileana', 1151, 4);")

# Define the query
query = "SELECT Department.NAME as 'Department Name', COUNT(Employee.ID) as 'Employee Count' FROM Department LEFT JOIN Employee ON Department.ID = Employee.DEPT_ID GROUP BY Department.NAME ORDER BY COUNT(Employee.ID) DESC, Department.NAME ASC;"

# Execute the query
cursor.execute(query)

# Fetch and print the desired results
results = cursor.fetchall()
for result in results:
    print(result)

# Close the cursor and the connection
cursor.close()
con.close()