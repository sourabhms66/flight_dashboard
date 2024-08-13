import pymysql

# Connect to database server
try:
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='rareview',
        database='indigo'  # if you want to connect to a specific database
    )
    mycursor = conn.cursor()
    print('connection established')
except:
    print('Connection error!')

# create a database on the db server
#mycursor.execute('CREATE DATABASE indigo')
#conn.commit()

# create a table
# airport -> airport_id | code | name

#mycursor.execute("""
#CREATE TABLE airport(
#    airport_id INT PRIMARY KEY,
#    code VARCHAR(10) NOT NULL,
#    name VARCHAR(255) NOT NULL,
#   city VARCHAR(50) NOT NULL
#)
#""")
#conn.commit()

# insert data in the airport table
#mycursor.execute("""
#    INSERT INTO airport VALUES
#    (1,'DEL','IGIA','New Delhi'),
#    (2,'CCU','NSBIA','Kolkata'),
#    (3,'BOM','CSMA','Mumbai')
#""")
#conn.commit()

# search/ retrieve
mycursor.execute("SELECT * FROM airport where airport_id>1")
data = mycursor.fetchall()
print(data)

# if we only want the cities

for i in data:
    print(i[3])

# update
# mycursor.execute("""
# UPDATE airport
# set city = 'Bombay' where city = 'Mumbai'
# """)
# conn.commit()
#
# # to see the change
#
# mycursor.execute("SELECT * FROM airport where airport_id>1")
# data = mycursor.fetchall()
# print(data)

# delete
# mycursor.execute("""
# DELETE FROM airport where city = 'Bombay'
# """)
# conn.commit()
# to see the change
#
# mycursor.execute("SELECT * FROM airport where airport_id>1")
# data = mycursor.fetchall()
# print(data)

