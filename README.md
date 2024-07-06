# Python DB Connection Files

This repository contains various Python scripts for connecting to and performing operations on a MySQL database. Below is a description of each script along with its functionality.

## 01_DB_Connection.py

This script connects to a MySQL database, retrieves data from the `employees` table, and prints the data in a formatted table using the `tabulate` library.

## 02_DB_Operation.py

This script demonstrates various database operations such as:

- Retrieving data from the `employees` table.
- Inserting new records into the `employees` table.
- Deleting records from the `employees` table.
- Updating existing records in the `employees` table.

It also includes the ability to list all databases on the MySQL server.

## 03_DB_Data_Export.py

This script retrieves data from the `employees` table and exports it to an Excel file. It also demonstrates how to send an email with the exported file as an attachment using the `smtplib` library.

## 04_DB_data_to_excel.py

This script connects to a MySQL database, retrieves data from the `employees` table, and saves it to an Excel file using the `pandas` library.

## 05_DB_sqlalchemy.py

This script demonstrates how to connect to a MySQL database using SQLAlchemy, define a table schema, and create the table in the database.
