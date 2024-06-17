import mysql.connector
import numpy as np
import pandas as pd
from tabulate import tabulate
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="login12*",
    database="demo"
)

myCursor = myDB.cursor()

myCursor.execute("select * from employees")
rows = myCursor.fetchall()



column_names = [i[0] for i in myCursor.description]
print(tabulate(rows, headers=column_names, tablefmt="pretty"))

data_list = [list(row) for row in rows]

numpy_array = np.array(data_list)

df = pd.DataFrame(numpy_array, columns=column_names)

df.to_excel("emp_data.xlsx", index=False)

print("Data saved to emp_data.xlsx")

myCursor.close()
myDB.close()