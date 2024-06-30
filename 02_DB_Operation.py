import mysql.connector  # using mysql connector 

myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shiva@123",
    database="demo"
)

print(myDB)


# Show all databases
myCursor = myDB.cursor()
myCursor.execute("show databases")
for db in myCursor:
    print(db)

print("-----------------------------------------------")


# Data retrieval 
print("Employee name and their role:")
myCursor.execute("select name, department from employees")
for emp in myCursor:
    print(emp)

print("-----------------------------------------------")


print("Employee name with years of experiance:")
myCursor.execute("select name, emp_yoe, emp_salary from employees")
for emp in myCursor:
    print(emp)

print("-----------------------------------------------")




# # Insert operation 
# myCursor.execute("insert into employees(id, name, emp_salary, emp_yoe, age, department) values(4, 'Sonu', 9000, 2, 26, 'Designer')" )
# for emp in myCursor:
#     print(emp)

# myDB.commit()
# print("Record inserted successfully")

# print("-----------------------------------------------")




# Delete opearation 
# myCursor.execute("delete from employees where id = 4")
# myDB.commit()
# print("Successfully Deleted")

# print("-----------------------------------------------")


# Update opearation 
# print("Role senior engineer changed to tech lead ")
# myCursor.execute("update employees set department = 'Junior Engineer' where id = 2")
# myDB.commit()

# print("Data Update Succcessfully")
# print("-----------------------------------------------")




if myDB.is_connected:
    db_info = myDB.get_server_info()
    print("Connected to MySQL Server version ", db_info)

    myCursor.execute("select database();")
    record = myCursor.fetchone()
    print("You're connected to database: ", record)

    myCursor.close()
    myDB.close()

else:
    print("You're not connected to MySQL Server") 