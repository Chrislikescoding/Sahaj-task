import sqlite3
# connect to database
conn = sqlite3.connect('orders.db')
# create a cursor
c = conn.cursor()

# create a Table for orders

c.execute("""CREATE TABLE IF NOT EXISTS orderheader(
order_id INTEGER PRIMARY KEY AUTOINCREMENT,
order_status TEXT,
item_count INTEGER
)""")
# create a Table for order products
c.execute("""CREATE TABLE IF NOT EXISTS orderdetail(
order_detail_id INTEGER,
product_name TEXT,
product_quantity INTEGER,
order_detail_status TEXT
)""")
# create a Table for  products
c.execute("""CREATE TABLE IF NOT EXISTS products(
product_name TEXT
)""")
# fill product table
c.execute("""INSERT INTO products  VALUES ('eggs'), ('apples'), ('coffee'), ('cake') ,
('bread') ,('milk'), ('newspaper'), ('book'),('cat food') """)

conn.commit()
conn.close()
