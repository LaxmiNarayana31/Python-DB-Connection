import mysql.connector
from tabulate import tabulate

try:
    myDB = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shiva@123",
        database="demo"
    )

    if myDB.is_connected():
        db_info = myDB.get_server_info()
        print("Connected to MySQL Server version ", db_info)

        myCursor = myDB.cursor()

        # Fetch employees table data
        myCursor.execute("SELECT * FROM employees")
        employees_data = myCursor.fetchall()

        # Define headers and print formatted table
        headers = ["ID", "Name", "Age", "Department", "Years of Experience", "Salary"]
        print("\nEmployees table:")
        print(tabulate(employees_data, headers=headers, tablefmt="grid"))

except mysql.connector.Error as e:
    print("Error connecting to MySQL:", e)

finally:
    if 'myCursor' in locals():
        myCursor.close()
    if 'myDB' in locals() and myDB.is_connected():
        myDB.close()
        print("MySQL connection is closed")
        