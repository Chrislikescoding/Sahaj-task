import sqlite3


class Order:

    def __init__(self, status, product_count):
        self.status = status
        self.product_count = product_count

    def create_order(self, status, product_count):
        order_created = False
        try:
            conn = sqlite3.connect('orders.db')
            # create a cursor
            c = conn.cursor()
            # insert into table
            c.execute("INSERT INTO orderheader (order_status,item_count)"
                      " VALUES ('{}',{})".format(status, product_count))
            last_row_id = c.lastrowid
            print("Order created with id {}".format(last_row_id))
            order_created = True
        except sqlite3.Error as error:
            print("Failed to insert data to create the order", error)
        finally:
            conn.commit()
            conn.close()
        return order_created
