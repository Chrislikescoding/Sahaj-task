# run this to clear all the files if you want to start again
import sqlite3
# connect to database
conn = sqlite3.connect('orders.db')
# create a cursor
c  =conn.cursor()
# create a Table

c.execute("""DROP TABLE orderheader""")
c.execute("""Drop TABLE  orderdetail""")
c.execute("""Drop TABLE  products""")

conn.commit()
conn.close()
