import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"     #if exists
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase") #create database

#show databases
'''
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
'''

# create tables
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
'''
# show tables
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)
'''
#add primary key using alter table command (use if table exists)
#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# insert a record
'''
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
'''

# insert multiple records
'''
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
'''
# use fetchone method to print first row or fetchall method to print all rows
'''
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()
#myresult = mycursor.fetchall()

print(myresult)
'''
# Prevent sql injection
#When query values are provided by the user, you should escape the values.
#This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
#The mysql.connector module has methods to escape query values:
'''
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
'''
print("Executed")
