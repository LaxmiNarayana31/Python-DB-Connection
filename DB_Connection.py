import mysql.connector

try:
    myDB = mysql.connector.connect(
        host="localhost",
        user="root",
        password="login12*",
        database="demo"
    )

    if myDB.is_connected():
        db_info = myDB.get_server_info()
        print("Connected to MySQL Server version ", db_info)

        myCursor = myDB.cursor()

        myCursor.execute("SHOW DATABASES")
        print("List of databases:")
        for db in myCursor:
            print(db)  

        myCursor.execute("SELECT DATABASE();")
        record = myCursor.fetchone()
        print("You're connected to database:", record)

except mysql.connector.Error as e:
    print("Error connecting to MySQL:", e)

finally:
    if 'myCursor' in locals():
        myCursor.close()
    if 'myDB' in locals() and myDB.is_connected():
        myDB.close()
        print("MySQL connection is closed")
