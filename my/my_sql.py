import sqlite3

connection=sqlite3.connect("Naresh_it_umapathi.db")

cursor=connection.cursor()

table_info="""
Create table Naresh_it_umapathi(employee_name varchar(30),
                    employee_role varchar(30),
                    employee_salary FLOAT);
"""
cursor.execute(table_info)

cursor.execute('''Insert Into Naresh_it_umapathi values('Omkar Nallagoni','Data Science',75000)''')
cursor.execute('''Insert Into Naresh_it_umapathi values('Naresh','Data Science',90000)''')
cursor.execute('''Insert Into Naresh_it_umapathi values('Phani','Data Science',88000)''')
cursor.execute('''Insert Into Naresh_it_umapathi values('Naga babu','Data Engineer',50000)''')
cursor.execute('''Insert Into Naresh_it_umapathi values('Ajay','Data Engineer',35000)''')
cursor.execute('''Insert Into Naresh_it_umapathi values('Pawan','Data Engineer',60000)''')



print("The isnerted records are")
data=cursor.execute('''Select * from Naresh_it_umapathi''')
for row in data:
    print(row)

#Commit your changes int he databse
connection.commit()
connection.close()